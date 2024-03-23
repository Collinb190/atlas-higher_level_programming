# Use Ubuntu as the base image
FROM ubuntu:20.04

# Install curl
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y curl

# Install Node.js 14
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash -
RUN apt-get install -y nodejs

# Install semistandard globally
RUN npm install semistandard --global

# Create a directory for your project in the container
WORKDIR /app

# Copy the contents of your local folder into the container
COPY . /app

# Set the default command to be executed when the container starts
CMD ["/bin/bash"]
