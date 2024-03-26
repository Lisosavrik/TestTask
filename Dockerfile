FROM python:3.11.3

WORKDIR /code

ADD . .

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./main.py" ]