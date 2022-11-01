FROM python:3

WORKDIR /app

COPY . .

RUN pip3 install -r requirenents.txt

EXPOSE 5000

CMD [ "python", "main.py" ]
