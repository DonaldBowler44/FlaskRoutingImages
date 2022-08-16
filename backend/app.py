from flask import Flask, request, render_template
from datetime import datetime
from flask_cors import CORS
from routes.uploads import upload
from model import db

def create_app():
    app = Flask(__name__)
    app.config['UPLOAD_DIRECTORY'] = 'uploads/'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:4donald5@localhost/baby-tracker'
    app.config["SECRET_KEY"] = '5f352379324c22463451387a0eeesddef'
    app.config['ALLOWED_EXTENSIONS'] = ['.jpg', '.jpeg', '.png', '.gif']

    CORS(app)
    db.init_app(app)
    app.register_blueprint(upload, url_prefix="")

    with app.app_context():
        db.create_all()

    @app.route('/target')
    def target_page():

        title="targetpage"
        context={
            'title':title
        }
        return render_template('target.html',**context)

    if __name__ == '__main__':
        app.run(debug=True)

    return app
