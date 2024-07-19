# single node GKE cluster
gcloud container clusters create fruicy \
--machine-type e2-medium \
--num-nodes 2 \
--disk-size 50

# Get all informations
#!/bin/bash

# Common command
common_command="kubectl get"

# List of arguments for the common command
args_list=(
    "pods"
    "deployments"
    "services"
)

# Loop through the list and execute the common command with each set of arguments
for args in "${args_list[@]}"; do
    $common_command $args
done
