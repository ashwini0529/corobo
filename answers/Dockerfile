FROM python:3

ENV ROOT=/app

ADD requirements.txt $ROOT/requirements.txt
ADD crontab /etc/cron.d/update_cron
RUN crontab /etc/cron.d/update_cron

RUN apt-get -y update && apt-get install -y gcc gfortran cron\
    && pip install -U pip -r $ROOT/requirements.txt \
    && apt-get remove -y gcc gfortran \
    && python -m spacy download en_core_web_md

ADD . $ROOT/answers

WORKDIR /app
CMD sh -c "cron -f && gunicorn -t 120 answers.service:app"
