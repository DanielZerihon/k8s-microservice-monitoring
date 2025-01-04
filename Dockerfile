# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy application code
COPY vm_metrics.py .

# Expose port and run the app
EXPOSE 5000
CMD ["python", "vm_metrics.py"]

