import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from datetime import datetime
from eralchemy2 import render_er

Base = declarative_base()

class Follower(Base):
    __tablename__ = 'follower'
    user_id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(250))
    dob = Column(DateTime)
    last_login_time = Column(DateTime)

class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True)

    user_from_id = Column(Integer, ForeignKey('user.user_id'))
    user_to_id = Column(Integer, ForeignKey('user.user_id'))
    followers = relationship("Follower", back_populates="user")

class Media(Base):
    __tablename__ = 'media'
    media_id = Column(Integer, primary_key=True)
    user_id1 = Column(Integer, ForeignKey('user.user_id'))
    user_id2 = Column(Integer, ForeignKey('user.user_id'))

class Post(Base):
    __tablename__ = 'post'
    feed_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    content = Column(String(250))
    photo_id = Column(Integer, ForeignKey('photo.photo_id'))
    creation_date = Column(DateTime, default=datetime.utcnow)
    photo = relationship("Photo", back_populates="post")

class Comment(Base):
    __tablename__ = 'comment'
    comment_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    content = Column(String(250))
    photo_id = Column(Integer, ForeignKey('photo.photo_id'))
    creation_date = Column(DateTime, default=datetime.utcnow)
    photo = relationship("Photo", back_populates="comment")

    def to_dict(self):
        return {}

class Photo(Base):
    __tablename__ = 'photo'
    photo_id = Column(Integer, primary_key=True)
    url = Column(String(250))
    post = relationship("Post", uselist=False, back_populates="photo")
    comment = relationship("Comment", uselist=False, back_populates="photo")

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem generating the diagram")
    raise e
