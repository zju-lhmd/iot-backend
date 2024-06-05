FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install /app

EXPOSE 8083

CMD ["python3", "mqttserver.py"]