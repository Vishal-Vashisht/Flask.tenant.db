from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
from flask_migrate import Migrate
import uuid
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String

db = SQLAlchemy()
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)\


class Post(Base):

    __tablename__ = "Post"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
# class UserCart(Base):
#     __tablename__ = 'user_cart'

#     id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
#     user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     name = db.Column(db.String)
#     email = db.Column(db.String)
#     gender = db.Column(db.String)
#     refrence_id = db.Column(db.Integer)

#     def save(self):
#         db.session.add(self)
#         try:
#             db.session.commit()
#         except Exception:
#             db.session.rollback()


# class UserApp(Base):
#     __tablename__ = "user_app"

#     id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
#     user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     name = db.Column(db.String)
#     email = db.Column(db.String)
#     gender = db.Column(db.String)
#     refrence_id = db.Column(db.Integer)

#     def save(self):
#         db.session.add(self)
#         try:
#             db.session.commit()
#         except Exception:
#             db.session.rollback()


# class UserAppPostData(Base):

#     __tablename__ = 'user_app_post_data'

#     id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
#     user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     name = db.Column(db.String)
#     email = db.Column(db.String)
#     gender = db.Column(db.String)
#     refrence_id = db.Column(db.Integer)
