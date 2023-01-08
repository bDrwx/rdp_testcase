FROM python:3.9-alpine

RUN mkdir /app
COPY rdp_testcase /app
COPY requirements.txt /app

WORKDIR /app
ENV PYTHONPATH=${PYTHONPATH}:${PWD}

RUN pip install -r requirements.txt

CMD ["python", "cli.py", "--port", "9191"]