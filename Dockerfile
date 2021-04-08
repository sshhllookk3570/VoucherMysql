from python3.6-slim

ENV USER shlok

RUN mkdir/con

workDIR /con

Run pip install --upgrade pip
RUN pip install django

COPY ./con/

EXPOSE 8000

CMD["python3","manage.py","runserver","127.0.0.1"]