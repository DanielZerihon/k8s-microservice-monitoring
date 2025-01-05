Home Assignment<br>
Overview<br><br>
This assignment requires you to containerize and deploy a microservice in Kubernetes,<br>
while also integrating Prometheus and Grafana for monitoring and visualization of the<br>
service metrics.<br><br>
The entire project should be designed to run on a Kubernetes environment (Can belocal environment using tools like k3s or k3d)<br>
Requirements:<br>
Here are the detailed requirements:<br>
1.	Microservice - You can choose an example microservice. make sure the service<br>
has metrics exposed, as you will need them for the Prometheus phase.<br>For
example, consider Nginx, or choose any image you find on the internet that fits the criteria.<br>
2.	kubernetes Manifest - You need to create Kubernetes manifest files to deploy the<br>
	microservice in a highly available setup.<br>
3.	Prometheus Scraping - You should set up a Prometheus service within the<br>
	Kubernetes cluster to collect and scrape metrics from the microservice.<br>
4.	Grafana Dashboard - Create a dashboard in Grafana to visualize the metrics<br>
	collected by Prometheus. Make sure to expose Grafana UI.<br>
5.	Github repo - All files should be stored in a GitHub repository, along with instructions on how to run your application.<br>
