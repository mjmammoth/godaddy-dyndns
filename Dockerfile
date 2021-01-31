FROM ubuntu:20.04
RUN apt-get update && \
apt-get install -y python3 python3-pip cron
RUN pip3 install requests godaddypy datetime
COPY godaddy-dyndns.py /
RUN chmod 0755 /godaddy-dyndns.py
COPY ddns-cron /
COPY entrypoint.sh /
RUN chmod 0755 entrypoint.sh
WORKDIR /
RUN crontab ddns-cron
ENTRYPOINT [ "/entrypoint.sh" ]
