#FROM python:3.6.8-alpine3.9

#LABEL MAINTAINER="Rik Bose <rbose@knox.edu>"

#ENV GROUP_ID=1000 \
#    USER_ID=1000

#WORKDIR /var/www/


#ADD ./requirements.txt /var/www/requirements.txt
#RUN pip install -r requirements.txt
#ADD . /var/www/
#RUN pip install gunicorn

#RUN addgroup -g $GROUP_ID www
#RUN adduser -D -u $USER_ID -G www www -s /bin/sh

#USER www

#EXPOSE 5000

# this is a backup command
# CMD ["flask", "run", "-h", "0.0.0.0", "--debugger"]
#CMD [ "gunicorn", "-w", "4", "--bind", "0.0.0.0:5000", "--log-level", "debug", "wsgi"]

FROM python:3.6.8-alpine3.9 
LABEL MAINTAINER="Rik Bose <rbose@knox.edu>" 
ENV GROUP_ID=1000 \
     USER_ID=1000 
WORKDIR /var/www/ 

RUN apk add --update --no-cache g++ gcc libxslt-dev libxml2-dev jpeg-dev zlib-dev 
ADD ./requirements.txt /var/www/requirements.txt 
RUN pip install -r requirements.txt 

#test locally to make sure this command will work on the backend droplet. 
RUN python -m nltk.downloader -d /usr/local/share/nltk_data all

ADD . /var/www/ 
RUN pip install gunicorn 

RUN addgroup -g $GROUP_ID www 
RUN adduser -D -u $USER_ID -G www www -s /bin/sh 

USER www 

EXPOSE 5000 
# this is a backup command # CMD ["flask", "run", "-h", "0.0.0.0", "--debugger"] 
CMD [ "gunicorn", "-w", "4", "--bind", "0.0.0.0:5000", "--log-level", "debug", "wsgi"]


#notes for restarting the droplet, does not affect database
#docker-compose down
#docker system prune -a
#docker-compose up -d

#delete database (right after docker-compose down command above)
#docker volume ls
#docker volume rm name_of_volume_to_remove

#Consider the cange that DK mentioned so we dont have to go throught all the above steps each time we want to change the droplet on digital ocean. 

#Debugging output coming from flask in container
#docker logs -f flask 