from flask import Flask

def create_app():
    app = Flask(__name__)

    # Import and register blueprint
    from app.routes.upload import upload_bp
    app.register_blueprint(upload_bp)

    # Home route
    @app.route("/")
    def home():
        return "Resume Analyzer API is running"

    return app