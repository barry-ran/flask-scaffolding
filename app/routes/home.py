import os
from flask import Blueprint, render_template, request, current_app
from ..models.ip_count import IpCount
from ..log import Log

home_bp = Blueprint('home_bp', __name__)

# 如果需要多个路径路由到通过一个函数，直接在此添加即可
# @home_bp.route('/index.html', methods=['GET', 'POST'])
@home_bp.route('/', methods=['GET', 'POST'])
def index():
    ip = request.remote_addr
    Log.logger().info('index request.remote_addr:%s', ip)

    if 'X-Forwarded-For' in request.headers:
        ip = request.headers['X-Forwarded-For']
        Log.logger().info("index request.headers['X-Forwarded-For']:%s", ip)

    count = IpCount.get_count(ip)
    count = count + 1
    IpCount.set_count(ip, count)

    Log.logger().info('index ip:%s count:%d', ip, count)

    if not current_app.config['PRODUCTION_CONFIG']:
        Log.logger().info("SECRET_KEY:%s", os.environ.get('SECRET_KEY'))

    return render_template('index.html', ip_count=count)