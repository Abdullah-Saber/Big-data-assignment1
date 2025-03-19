# Use Ubuntu as the base image
FROM ubuntu:latest

# Update package list and install Python3 and essential packages
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip

# Install Python libraries using pip with the break-system-packages flag
RUN pip3 install --break-system-packages pandas numpy seaborn matplotlib scikit-learn scipy

# Create the directory inside the container
RUN mkdir -p /home/doc-bd-a1/

RUN ln -sf /usr/bin/python3 /usr/bin/python || true

# Copy the dataset into the container directory
COPY top_rated_movies\(tmdb\).csv /home/doc-bd-a1/

# Set the working directory
WORKDIR /home/doc-bd-a1/

# Open bash shell on container startup
CMD ["/bin/bash"]
