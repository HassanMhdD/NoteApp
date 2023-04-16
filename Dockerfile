#########################################################
# Dockerfile to build Flask App
# Based on 
#########################################################

# Set the base image
FROM ubuntu
ENV TZ=Europe/Paris
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
RUN apt-get update && apt install apache2 python3 pip libpq-dev apache2-dev -y \ 
        && pip3 install --upgrade pip
# Copy over and install the requirements
COPY --chmod=777 ./NoteApp/app /var/www/app
RUN  pip install -r /var/www/app/requirements.txt 
RUN mv /var/www/app/flask-noteapp.conf /etc/apache2/sites-available/


RUN pip install mod_wsgi
RUN mod_wsgi-express module-config > /etc/apache2/mods-available/wsgi.load
RUN a2enmod wsgi
RUN a2dissite 000-default.conf
RUN a2ensite flask-noteapp.conf

# LINK apache config to docker logs
RUN ln -sf /proc/self/fd/1 /var/log/apache2/access.log &&\ 
        ln -sf /proc/self/fd/1 /var/log/apache2/error.log

EXPOSE 80
 

# Start  Apache web server when the container launches
#CMD service apache2ctl -D FOREGROUND
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]