FROM python:3.11-slim

# Enable docker mode
ENV DOCKER_MODE true

# Create working directory
WORKDIR /app

# Copy sources
COPY frontend/ app/frontend/
COPY notebooks/ app/notebooks/
COPY server/ app/server/

RUN pip3 install --no-cache-dir --upgrade -r app/server/requirements.txt

CMD ["python3.11", "app/server/main.py"]
