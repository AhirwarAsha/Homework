# Homework
This DevOps project involving Kubernetes, MySQL replication, monitoring, and high availability.
Below is a breakdown of my approch to implement each requirement.
1. Project Structure
   
   devops-project/
│── infra/                  # Infrastructure as Code (IaC)
│   ├── k8s/                # Kubernetes manifests
│   │   ├── mysql-master.yaml
│   │   ├── mysql-slave.yaml
│   │   ├── writer-deployment.yaml
│   │   ├── reader-deployment.yaml
│   │   ├── service.yaml
│   │   ├── ingress.yaml
│   ├── monitoring/         # Prometheus & Grafana
│   │   ├── prometheus-config.yaml
│   │   ├── grafana-dashboard.yaml
│── scripts/                # Deployment & automation scripts
│   ├── setup-cluster.sh
│   ├── deploy-apps.sh
│   ├── stress-test.sh
│── src/                    # Application code
│   ├── writer.py
│   ├── reader.py
│── Dockerfile               # Docker image setup
│── README.md                # Instructions

1. Infrastructure Setup:
* Use Infrastructure-as-Code (IaC) with Kubernetes manifests, Helm, and scripts.

2. Kubernetes Cluster (Minikube/kind)
* Use kind or minikube to create a single-node cluster.
* Write a script (setup-cluster.sh) to automate cluster setup.

Command: kind create cluster --name devops-cluster

3. MySQL Master-Slave Deployment
* Deploy MySQL Master and MySQL Slave as separate pods.
* Configure automatic replication between master and slave.
* Ensure replication persists after pod restarts.
* Use Kubernetes Secrets for credentials.

4. Writer & Reader Applications
* Runs in a separate pod.
* Generates and inserts data into MySQL Master every 1 second.
* Measures and exports response time as Prometheus metrics.

5. Reader Program
* Runs as 3 replicas in a Kubernetes Deployment.
* Queries MySQL Slave every 1 second for row count.
* Exposes an HTTP API to return row count & pod name.
* Measures query response time as Prometheus metrics.
* Ensures high availability by continuing to serve traffic even if a pod is deleted.

6. Monitoring & Observability
* Deploy Prometheus to scrape metrics from Reader and Writer.
* Deploy Grafana to visualize response time metrics.
* Create Grafana dashboards to monitor:
   - Query response times
   - Writer insert response times
   - API availability & performance

7. Automated Deployment
* Infrastructure-as-Code (Kubernetes manifests, Helm, Terraform, or scripts).
* CI/CD pipeline to build and deploy Docker images.
* Script for :
      - create the Minikube/kind cluster.
      -Build & deploy all components (MySQL, Writer, Reader, Monitoring).
      -Open Grafana for verification.
  
8. API Stress Testing & Rolling Updates
* Use k6 or Apache JMeter for HTTP stress testing.
* During stress testing:
     - Trigger a rolling update by modifying the Reader deployment.
     - Ensure zero downtime during pod restarts.
  



