#!/bin/bash
cachedcount=$(tail -n 100 /godaddy-dyndns-logs | grep -c 'Cached IP file exists')
if (($cachedcount > 2)); then
  pkill tail
  exit 1;
else 
  exit 0; 
fi
