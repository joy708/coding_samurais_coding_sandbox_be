# Use an existing base image as a starting point
FROM ubuntu:20.04

# Run commands to install software or configure the image
RUN apt-get update && apt-get install -y \
    python3 \
    g++
CMD ["/bin/bash"]