#base image
FROM python:3.7

#working directory
WORKDIR /app

#code
COPY . /app

#instal libraries
RUN pip install -r requirements.txt

#migrations
RUN python cool_counters/manage.py migrate

#run app
CMD ["python","cool_counters/manage.py","runserver","0.0.0.0:8000"]