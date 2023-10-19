# syntax = docker/dockerfile:1
FROM python:3.10-bullseye
COPY /src /src
RUN pip install requests
CMD ["python", "/src/bitcoin_pricing_app.py"]