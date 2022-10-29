FROM python:3.11-slim

# Enable docker mode
ENV DOCKER_MODE true

# Create working directory
WORKDIR /app

# Copy sources
COPY frontend/ ./frontend
COPY notebook/ ./notebook
COPY main.py ./
COPY service.py ./
COPY database.py ./
COPY models.py ./


# Copy and install Pip deps
COPY requirements.txt ./
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

CMD ["python3", "main.py"]
