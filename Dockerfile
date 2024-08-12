FROM python:3.11

WORKDIR /usr/src/app

COPY requirements.txt .

RUN apt-get update && apt-get install -y cron

RUN touch /var/log/cron.log

RUN pip install --no-cache-dir -r requirements.txt

COPY /src .

RUN sh -c 'echo "$CRON_SCHEDULE /usr/bin/python3 /usr/src/app/getReadings.py >> /var/log/cron.log 2>&1" > /etc/cron.d/get-readings-cron'

RUN chmod 0644 /etc/cron.d/get-readings-cron

RUN crontab /etc/cron.d/get-readings-cron

EXPOSE 19991

ENV UDEV=1

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "19991"]