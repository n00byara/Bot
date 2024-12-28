FROM python:3.13.0
WORKDIR /usr/app
COPY requirements.txt /usr/app
RUN pip install -r requirements.txt
CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3000", "--reload" ]