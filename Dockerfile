FROM python:3.10
LABEL authors="dima"

WORKDIR /project

COPY ./requirements.txt /project/requirements.txt

#RUN apk install netcat gcc postgresql
RUN pip install --no-cache-dir --upgrade -r /project/requirements.txt

EXPOSE 8000:8000

COPY ./app /project/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--reload"]
