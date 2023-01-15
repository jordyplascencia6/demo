FROM python:3.9-alpine

WORKDIR /App

ENV FLASK_APP App.py
ENV FLASK_RUN_HOST 0.0.0.0

COPY . .

RUN pip install -r requirements.txt

CMD [ "python3", "App.py" ]