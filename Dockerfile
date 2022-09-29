# Stage 1: Builder/Compiler
FROM python:3.8-slim as builder
RUN apt update && \
    apt install --no-install-recommends -y build-essential gcc
COPY requirements.txt /requirements.txt

RUN pip install --no-cache-dir --user -r /requirements.txt

# Stage 2: Runtime
FROM debian:buster-slim
RUN apt update && \
    apt install --no-install-recommends -y build-essential python3 && \
    apt clean && rm -rf /var/lib/apt/lists/*
COPY --from=builder /root/.local/lib/python3.7/site-packages /usr/local/lib/python3.7/dist-packages
COPY . /src
CMD ["python3", "/src/main.py"]
EXPOSE 5000
