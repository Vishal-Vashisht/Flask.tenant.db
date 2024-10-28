from flask import Flask, jsonify, Response, g, request
from config.redis_config import redis_client
# from app.api.controllers.user_controller import auth_bp
# from app.api.controllers.convert_type_controller import convert_bp
from app.api.models.models import db, User
from app.middelware import TenantConnectionMiddleware
# from app.api.models.models import TestCaseQuery
from flask_cors import CORS
from sqlalchemy.orm import sessionmaker


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object("config.dev")
    # redis_client.init_app(app)
    CORS(app)
    db.init_app(app)
    # migrate.init_app(app, db)
    # app.register_blueprint(auth_bp)
    # app.register_blueprint(convert_bp)
    @app.route("/", methods=['GET', 'POST', 'PUT'])
    def create_user():

        new_user = User(name="vishal")

        try:
            print("db", db)
            g.session.add(new_user)
            g.session.commit()

            users = g.session.query(User).all()
            for user in users:
                print(user.name)
            return jsonify({"message": "User created", "id": new_user.id}), 201
        except Exception as e:
            g.session.rollback()  # Rollback in case of error
            return jsonify({"error": str(e)}), 500

    @app.before_request
    def before_request_func():
        middleware = TenantConnectionMiddleware(app)
        response = middleware()
        if isinstance(response, tuple):  # Check if a response is returned
            return response
    return app
