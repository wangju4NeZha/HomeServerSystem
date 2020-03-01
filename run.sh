#!/bin/bash

cd /usr/src
gunicorn -w 1 -b 0.0.0.0:8000 homems.wsgi
echo "服务器已启动"
