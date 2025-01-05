Home Assignment 
Overview 

This assignment requires you to containerize and deploy a microservice in Kubernetes , 
while also integrating Prometheus and Grafana for monitoring and visualization of the 
service metrics . 
The entire project should be designed to run on a Kubernetes environment (Can be 
local environment using tools like k3s or k3d) 

Requirements : 
Here are the detailed requirements : 

1. Microservice - You can choose an example microservice. make sure the service 
has metrics exposed, as you will need them for the Prometheus phase. For 
example, consider Nginx, or choose any image you find on the internet that fits the 
criteria .

3. kubernetes Manifest - You need to create Kubernetes manifest files to deploy the 
microservice in a highly available setup .

5. Prometheus Scraping - You should set up a Prometheus service within the 
Kubernetes cluster to collect and scrape metrics from the microservice .

7. Grafana Dashboard - Create a dashboard in Grafana to visualize the metrics 
collected by Prometheus. Make sure to expose Grafana UI .

9. Github repo - All files should be stored in a GitHub repository, along with 
instructions on how to run your application . 
