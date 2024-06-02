FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install /app

EXPOSE 8081

CMD ["gunicorn", "-b", "0.0.0.0:8081", "iotdevice:create_app('production')"]