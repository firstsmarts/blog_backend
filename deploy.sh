#!/usr/bin/env bash
# ssh -P 22022 root@47.98.51.239 rm -rf /opt/myweb_backend
# echo "rm done"
scp -P 22022 -r myweb_backend root@47.98.51.239:/opt/
echo 'upload done'

sleep 1
