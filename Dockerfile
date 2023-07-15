FROM python:3.10

RUN mkdir /insurance_app

WORKDIR insurance_app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x docker/*.sh

CMD gunicorn src.main:app --bind=0.0.0.0:8000

