from flask import Blueprint, render_template, request
from ..models.ip_count import IpCount
from ..log import Log

home_bp = Blueprint('home_bp', __name__)

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
    

    return render_template('index.html', ip_count=count)