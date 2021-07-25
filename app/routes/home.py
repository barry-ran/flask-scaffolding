from flask import Blueprint, render_template, request
from ..models.ip_count import IpCount

home_bp = Blueprint('home_bp', __name__)

@home_bp.route('/', methods=['GET', 'POST'])
def index():
    ip = request.remote_addr
    count = IpCount.get_count(ip)
    IpCount.set_count(ip, count + 1)

    return render_template('index.html', ip_count=count)