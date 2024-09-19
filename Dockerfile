FROM python:3.10-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY app.py /app
COPY requirements.txt /app
COPY functions.py /app
# RUN pip install --no-binary :all: Polygon3
RUN apt-get update
RUN apt-get install build-essential -y
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install\
    libgl1\
    libgl1-mesa-glx \ 
    libglib2.0-0 -y && \
    rm -rf /var/lib/apt/lists/*
RUN apt-get update && apt-get install -y libgl1 
# RUN pip uninstall opencv-python
# RUN pip install opencv-python-headless
# Run the command to install any necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run hello.py when the container launches
CMD ["python", "app.py"]