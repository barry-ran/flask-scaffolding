import os
from flask import Blueprint, render_template, send_from_directory
from ..log import Log

# https://blog.csdn.net/kaever/article/details/116312794?spm=1001.2014.3001.5501

log_list_bp = Blueprint('log_list_bp', __name__)

basedir = os.path.abspath(os.path.dirname(__file__))
logs_dir = os.path.join(basedir, '../logs')
        
@log_list_bp.route('/logs', methods=['GET', 'POST'])
def log_list():
    names = os.listdir(logs_dir)
    files = {}
    for name in names:
        path = os.path.join('/logs', name)
        Log.logger().info("list log file:%s", path)
        files.update({name:path})

    return render_template('log_list.html', files=files)

@log_list_bp.route('/logs/<filename>')
def download(filename):
    Log.logger().info("send file:%s:%s", logs_dir, filename)
    return send_from_directory(logs_dir, filename)