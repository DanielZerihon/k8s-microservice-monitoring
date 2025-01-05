# Kubernetes Microservice Monitoring with Prometheus and Grafana operators 

![image](https://github.com/user-attachments/assets/a0a4ac2c-6316-4493-a6b9-f0b000bc826b)




This repository contains a k8s Flask-based microservice that exposes system metrics in Prometheus format and publish metrics in grafana dashboard. The microservice is containerized and deployed in a Kubernetes environment using Helm charts. Prometheus is used to scrape these metrics, and Grafana provides a visual representation via a custom dashboard.

## Features

1. **Flask-based Microservice**: Exposes CPU and RAM metrics at the `/metrics` endpoint in Prometheus format.
2. **Highly Available Kubernetes Deployment**: Uses a Helm chart to deploy the microservice with multiple replicas.
3. **Prometheus Integration**: Scrapes the metrics exposed by the microservice.
4. **Grafana Dashboard**: Visualizes the metrics collected by Prometheus.

---

## Project Structure

```
├── vm_metrics.py             # Flask app exposing system metrics
├── Dockerfile                # Dockerfile for build the application
├── requirements.txt          # Python dependencies
├── k8s-helm-chart/           # Helm chart for deploying the microservice
│   ├── templates/            # Kubernetes manifests (deployment, service)
│   └── values.yml            # Configuration for the Helm chart
└── README.md                 # Project documentation
```

---

## Prerequisites

- **Docker**: For building the microservice image.
- **Kubernetes**: A local cluster (using `k3s` or `k3d`).
- **Helm**: To manage the deployment.
- **kubectl**: To interact with the Kubernetes cluster.
- **Prometheus and Grafana Operators**: For monitoring and visualization.

---

## Setup Instructions

### 1. Build and Push Docker Image

```bash
docker build -t <your dockerHub regestry>/k8s-microservice-monitoring .
docker push <your dockerHub regestry>/k8s-microservice-monitoring:latest
```

---

### 2. Deploy Prometheus and Grafana Operators

Before deploying the microservice, ensure Prometheus and Grafana operators are installed in your Kubernetes cluster. Use Helm to deploy them:

#### Install Prometheus Operator

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm install prometheus prometheus-community/kube-prometheus-stack
```

#### Install Grafana Operator

```bash
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update
helm install grafana grafana/grafana
```

Check the status of Prometheus and Grafana:

```bash
kubectl get pods
```

---

### 3. Deploy the Microservice Using Helm

Navigate to the `k8s-helm-chart` directory and deploy the microservice:

```bash
cd k8s-helm-chart/
helm install monitor-flask-app .
```

---

### 4. Access the Services

#### Access Prometheus


1. Expose the Prometheus service externally using a NodePort:
   ```bash
   kubectl expose service prometheus-server --type=NodePort --target-port=9090 --name=prometheus-server-ext

2. Open the port on your EC2 security group.
3. 
4. Open your browser and go to (http://<ec2-public-ip>:<PORT>).

#### Access Grafana

1. Expose the Grafana service externally using a NodePort:
   ```bash
   kubectl expose service grafana --type=NodePort --target-port=3000 --name=grafana-ext
   ```
2. Open the port on your EC2 security group.
3. Open your browser and go to (http://<ec2-public-ip>:<PORT>).
4. Use the default credentials:
   - **Username**: `admin`
   - **Password**: `secret pasword provide from grafana operator`

---

## Exposed Metrics

The microservice exposes the following system metrics at the `/metrics` endpoint:

- **`cpu_used`**: Percentage of CPU usage.
- **`ram_used`**: Percentage of RAM usage.
- **`ram_available`**: Percentage of available RAM.

---

## Configuration

You can customize the Helm chart by modifying `values.yml`. Key parameters include:

- **replicaCount**: Number of microservice replicas.
- **image.repository**: Docker image repository.
- **service.type**: Kubernetes service type (e.g., `ClusterIP`, `NodePort`).

---

## Additional Commands

### Uninstall the Microservice

```bash
helm uninstall monitor-flask-app
```

### Upgrade the Microservice

```bash
helm upgrade monitor-flask-app .
```

---

## Conclusion

This project demonstrates how to containerize a microservice, deploy it in Kubernetes, and set up monitoring and visualization using Prometheus and Grafana operators. 
It provides a scalable and observable solution suitable for real-world applications.

---
