# Use Ubuntu as the base image
FROM ubuntu:20.04

# Update package lists and install Node.js
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y nodejs npm

# Install semistandard globally
RUN npm install semistandard --global

# Create a directory for your project in the container
WORKDIR /app

# Copy the contents of your local folder into the container
COPY . /app

# Set the default command to be executed when the container starts
CMD ["/bin/bash"]
