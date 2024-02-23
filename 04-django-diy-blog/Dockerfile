FROM python:3.12.2-bullseye
ENV PYTHONUNBUFFERED 1

RUN apt update && apt install -y gettext

COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt

WORKDIR /code

COPY ./compose/entrypoint /entrypoint
COPY ./compose/start /start

RUN sed -i 's/\r//' /start && chmod +x /start && sed -i 's/\r//' /entrypoint && chmod +x /entrypoint


ENTRYPOINT ["/entrypoint"]
