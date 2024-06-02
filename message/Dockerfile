FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install /app

EXPOSE 8082

CMD ["gunicorn", "-b", "0.0.0.0:8082", "iotmessage:create_app('production')"]