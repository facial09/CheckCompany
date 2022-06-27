from flask import Flask

def create_app():

    app = Flask(__name__)


    from flask_app.routes import main_route

    app.register_blueprint(main_route.bp)
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True,port=5001)