#!/bin/bash
printenv | grep -v "no_proxy" >> /etc/environment
cron start
tail -f /godaddy-dyndns-logs
