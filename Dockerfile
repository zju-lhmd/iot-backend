FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install /app

EXPOSE 8080

CMD ["gunicorn", "-b", "0.0.0.0:8080", "iotauth:create_app('production')"]