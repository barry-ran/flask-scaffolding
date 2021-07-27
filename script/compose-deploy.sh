#!/bin/bash
docker-compose down
# 不带-d，调试用
# docker-compose up --build
docker-compose up -d --build
