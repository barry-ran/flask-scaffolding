#!/bin/bash
# 先尝试迁移数据库
flask db init -d ./app/migrations
flask db migrate -d ./app/migrations
flask db upgrade -d ./app/migrations
# 再启动supervisord
/usr/bin/supervisord
