#!/bin/bash

# Start Kubernetes Cluster
kind create cluster --name devops-cluster

# Deploy MySQL
kubectl apply -f mysql-secret.yaml
kubectl apply -f mysql-master.yaml
kubectl apply -f mysql-slave.yaml

# Deploy Applications
kubectl apply -f writer-deployment.yaml
kubectl apply -f reader-deployment.yaml
kubectl apply -f reader-service.yaml

# Deploy Monitoring
kubectl apply -f prometheus.yaml
kubectl apply -f grafana.yaml

# Open Grafana Dashboard
echo "Grafana running at: http://localhost:3000"
