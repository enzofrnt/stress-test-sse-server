FROM python:3.12.4-alpine3.20

WORKDIR /test

RUN apk add --no-cache gcc musl-dev libffi-dev

RUN rm -rf /var/cache/apk/*

COPY ./requirements.txt .

RUN pip install -r requirements.txt

RUN rm ./requirements.txt

COPY ./test .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
