# single node GKE cluster
gcloud container clusters create fruicy \
--machine-type e2-medium \
--num-nodes 1 \
--disk-size 50