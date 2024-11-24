#!/bin/bash

# 安装依赖
pip install -r requirements.txt

# 启动 Gunicorn
gunicorn --bind 0.0.0.0:8000 \
         --workers 4 \
         --timeout 120 \
         --access-logfile logs/access.log \
         --error-logfile logs/error.log \
         wsgi:app
