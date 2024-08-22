# Use an official Python runtime as a parent image
FROM python:3.10

# Set the docker working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages
RUN apt-get update && apt-get install -y wget
RUN pip install pandas requests psycopg2 sqlalchemy requests

# Run the main.py script
CMD ["python", "main.py"]

# Make pipeline.py executable and provide as an entrypoint
ENTRYPOINT ["python", "pipeline.py"]
