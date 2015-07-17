FROM mysql

ENV MYSQL_ROOT_PASSWORD=testing
ENV MYSQL_DATABASE=test

COPY entrypoint.sh /entrypoint.sh
RUN /entrypoint.sh mysqld

#RUN mkdir /etc/mysql/conf.d

EXPOSE 3306
CMD ["mysqld"]
