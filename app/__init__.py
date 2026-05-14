from flask import Flask # type: ignore

def create_app():
    app = Flask(__name__)

    from app.routes.home_routes import home_bp
    from app.routes.auth_routes import auth_bp
    from app.routes.dashboard_routes import dashboard_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)

    return app