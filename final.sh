#!/bin/bash

# Define variables
CONTAINER_NAME="hish"  # Replace with your actual container name or ID
DEST_DIR="service-result"  # Local directory to store the results

# Create the destination directory if it doesn't exist
mkdir -p $DEST_DIR

# Copy output files from container to local machine
docker cp ${CONTAINER_NAME}:/home/doc-bd-a1/res_dpre.csv $DEST_DIR/
docker cp ${CONTAINER_NAME}:/home/doc-bd-a1/eda-in-1.txt $DEST_DIR/
docker cp ${CONTAINER_NAME}:/home/doc-bd-a1/eda-in-2.txt $DEST_DIR/
docker cp ${CONTAINER_NAME}:/home/doc-bd-a1/eda-in-3.txt $DEST_DIR/
docker cp ${CONTAINER_NAME}:/home/doc-bd-a1/vis.png $DEST_DIR/
docker cp ${CONTAINER_NAME}:/home/doc-bd-a1/k.txt $DEST_DIR/

# Stop the container
docker stop ${CONTAINER_NAME}

echo "All output files have been copied to ${DEST_DIR} and the container has been stopped."
