#base image
FROM python:3.11-slim
#working directory
WORKDIR /app
#copy code
COPY . /app
#python dependencies
RUN pip install -r requirements.txt
#Make port 5000 available to the world outside of this container
EXPOSE 5000
#run code
CMD ["python","app.py"]
