FROM python:3.7

WORKDIR /dash-app

EXPOSE 9000

ADD . /dash-app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

CMD ["python", "app.py"]