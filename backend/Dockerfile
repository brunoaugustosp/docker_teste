FROM python:alpine3.9


COPY . /app

WORKDIR /app

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

EXPOSE 5000

# ENTRYPOINT [ "python" ]

# CMD ["app.py"]
# CMD playwright install
CMD gunicorn --bind 0.0.0.0:5000 app:app  
