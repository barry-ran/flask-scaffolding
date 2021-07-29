from flask import Blueprint, request
from ..log import Log

import requests
import random

girls_bp = Blueprint('girls_bp', __name__)

@girls_bp.route('/girls', methods=['GET', 'POST'])
def girls():
    Log.logger().info('recv girls request type:%s', request.method)
    # GET上传的数据用request.args获取，POST上传的数据用request.form获取
    if request.method == 'GET':
        data = request.args
    else:
        data = request.form
 
    Log.logger().info('recv girls request data:%s', data)
    return get_girls()

def get_girls():
    try:
        t = random.randint(10000000000000000, 99999999999999999)
        url = 'http://wmsp.cc/video.php?_t=0.{}'.format(t)
        header = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:21.0) Gecko/20100101 Firefox/21.0'
        }
        Log.logger().info('request girls url:%s', url)
        resp = requests.get(url, headers=header, allow_redirects=False)
        Log.logger().info('request girls resp:%s', resp.headers)
        return resp.headers['Location']
    except Exception as e:
        Log.logger().error('failed request girls:%s', e)
        return './demo.mp4'