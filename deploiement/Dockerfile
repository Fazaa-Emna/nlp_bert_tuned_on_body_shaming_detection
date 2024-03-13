FROM python:3.7.9

RUN apt -y update

COPY ./requirements.txt  ./root/workspace/requirements.txt

RUN pip install --upgrade pip

RUN pip install -r ./root/workspace/requirements.txt


CMD ["uvicorn", "root.workspace.main:app", "--host", "0.0.0.0", "--port", "8999"]
