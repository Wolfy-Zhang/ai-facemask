from flask import Flask

def create_app(config_type):  # 封装web应用的创建过程
    app = Flask(__name__)
    app.secret_key = b'_5#y2L"dfg8z\n\45:]/'
   
    # 注册蓝图对象  如果内容只在文件中使用一次, 最好在使用前才导入, 可以有效避免导入错误
    from controller.modules.home import home_blu
    app.register_blueprint(home_blu)
    from controller.modules.user import user_blu
    app.register_blueprint(user_blu)
    
    return app
