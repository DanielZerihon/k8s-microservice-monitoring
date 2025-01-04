from flask import Flask, Response
import psutil
import os

app = Flask(__name__)

@app.route('/metrics')
def metrics():
    # Collecting system stats
    cpu_used = round(float(os.popen('''grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage }' ''').readline()), 1)
    ram_used = psutil.virtual_memory().percent
    ram_available = round(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total, 1)
    number_of_sessions = round(float(os.popen('''who | wc -l''').readline()), 1)

    # Prometheus metrics formatted correctly
    metrics = f"""# HELP cpu_used CPU usage in percentage
# TYPE cpu_used gauge
cpu_used {cpu_used}

# HELP ram_used RAM usage percentage
# TYPE ram_used gauge
ram_used {ram_used}

# HELP ram_available RAM available percentage
# TYPE ram_available gauge
ram_available {ram_available}"""

    # Return the metrics as plain text for Prometheus to scrape
    return Response(metrics, mimetype='text/plain')

if __name__ == '__main__':
    # Run the Flask app on all network interfaces
    app.run(host='0.0.0.0', port=5000)

