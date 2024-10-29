#base image
FROM python:3.9
#working directory
RUN mkdir -p /app/persistentdata
WORKDIR /app
#Copy requirements.txt
COPY requiremnets.txt .
RUN pip install --no-cache-dir -r requiremnets.txt


#copy full code
COPY . .

#run django migrations 
RUN python manage.py makemigrations
RUN python manage.py migrate

#command to start django server
CMD ["python" , "manage.py" , "runserver" , "0.0.0.0:8000"]

