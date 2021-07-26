# flask-scaffolding
flask项目脚手架，可以基于此脚手架快速开发，减少重复操作

# 使用[pipenv](https://pipenv.pypa.io/en/latest/)管理依赖
```
pipenv install  # 创建虚拟环境并安装依赖（只有第一次搭建环境需要安装）
pipenv shell  # 激活虚拟环境
pipenv lock -r > ./app/requirements.txt # 导出所有依赖到requirements
pip freeze > requirements.txt # 导出所有依赖到requirements (两种方法都可以)
```
# 初始化数据库
```
flask db init  # 第一次初始化数据库升级环境
flask db migrate -m "Initial migration." # 更改数据库结构
flask db upgrade # 升级数据库（将上述修改应用到实际数据库中）
```

# vscode作为开发IDE
1. 安装[python插件](https://code.visualstudio.com/docs/python/python-tutorial)

2. 在左下角切换python环境为pipenv创建的环境：
    ![](docs/image/select-pipenv.png)
3. 调试运行：在左侧调试tab里可以通过Run and Debug来调试
    ![](docs/image/run-debug1.png)
    以flask方式运行时，需要指定我们flask app所在的python文件
    ![](docs/image/run-debug2.png)
    不想每次指定要运行的python文件可以create a launch.json来设置启动参数，注意环境指定：
    - FLASK_APP中指定的是业务逻辑上的环境（例如不同环境的数据库配置）
    - FLASK_ENV指定的是flask的环境（development环境会默认开启DEBUG模式），flask 1.0以后只能使用环境变量的方式配置环境
    DEBUG模式默认会启动debugger（发生错误时直接在网页中显示代码错误信息，并且可以直接shell调试），可以通过args中添加"--no-debugger"来关闭debugger
    ```
    {
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Flask",
            "type": "python",
            "request": "launch",
            "module": "flask",
            "env": {
                "FLASK_APP": "app:create_app('development')",
                "FLASK_ENV": "development"
            },
            "args": [
                "run"
            ],
            "jinja": true
        }
    ]
}
    ```
4. 运行单个python文件：可以在python文件右上角直接run python file in terminal
    ![](docs/image/run-python.png)


# 参考文档
- [flask项目的结构](https://lepture.com/en/2018/structure-of-a-flask-project)
- [Flask项目结构模板(主要参考这个)](https://www.justdopython.com/2020/01/18/python-web-flask-project-125/)
- [Flask 从入门到放弃6: 网站结构最佳实践(来自狗书第七章：大型程序的结构)](https://lvraikkonen.github.io/2017/08/28/Flask%20%E4%BB%8E%E5%85%A5%E9%97%A8%E5%88%B0%E6%94%BE%E5%BC%836:%20%E7%BD%91%E7%AB%99%E7%BB%93%E6%9E%84%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5/)
- [python vscode环境搭建](https://zhuanlan.zhihu.com/p/64994681)
- [使用 flask migrate 来迁移数据结构](https://einverne.github.io/post/2018/05/flask-migrate-tutorial.html)
- [flask_sqlalchemy增删改查](https://blog.csdn.net/Co_zy/article/details/77937195)
- [flask写日志](https://blog.csdn.net/qq_36441027/article/details/111182467)
- [flask错误处理](https://dormousehole.readthedocs.io/en/latest/errorhandling.html)
- [docker部署python](https://docs.docker.com/language/python/build-images/)
- [Deploy flask app with nginx using gunicorn and supervisor](https://medium.com/ymedialabs-innovation/deploy-flask-app-with-nginx-using-gunicorn-and-supervisor-d7a93aa07c18)
- [用docker部署flask+gunicorn+nginx](https://www.cnblogs.com/xuanmanstein/p/7692256.html)

# TODO
- dotenv配置敏感信息
- 生产启动
  - supervisor
- 文档整理
- 在线日志
