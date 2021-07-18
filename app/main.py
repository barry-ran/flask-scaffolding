from flask import Flask, render_template

# 用flask run命令启动app/main时会自动探测到我们创建的这个app对象来启动服务器
# 更多flask run的知识可以看这里：https://dormousehole.readthedocs.io/en/latest/cli.html
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    # 仅仅直接python main.py运行的时候才会通过这里启动服务器
    app.run(port=5000)