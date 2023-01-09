FROM python:3.9-alpine

RUN mkdir /app
COPY rdp_testcase /app/rdp_testcase
COPY requirements.txt /app

WORKDIR /app
ENV PYTHONPATH=${PYTHONPATH}:${PWD}

RUN pip install -r requirements.txt

CMD ["python", "rdp_testcase/cli.py", "--port", "9191"]