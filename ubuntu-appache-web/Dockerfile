FROM ubuntu
#WORKDIR /home/pak/app 

RUN apt-get update -y
RUN apt-get install apache2 -y

COPY index.html /var/www/html/
EXPOSE 80
#base image is ubuntu-->it has no CMD/entrypoint script--isliye CMD likhgan must tha ider or you can use docker run with -it 
CMD ["apachectl", "-D", "FOREGROUND"]
