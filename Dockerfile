FROM python:alpine

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

RUN sudo apt install python-pytest

EXPOSE 5000

CMD [ "python", "main.py" ]