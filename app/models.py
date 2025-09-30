from flask_login import UserMixin
import bcrypt
from app import db

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(60))  # bcrypt хеш всегда 60 символов

    def set_password(self, password):
        pwd_bytes = password.encode('utf-8')
        salt = bcrypt.gensalt()
        hash_bytes = bcrypt.hashpw(pwd_bytes, salt)
        self.password_hash = hash_bytes.decode('utf-8')

    def check_password(self, password):
        pwd_bytes = password.encode('utf-8')
        hash_bytes = self.password_hash.encode('utf-8')
        return bcrypt.checkpw(pwd_bytes, hash_bytes)

    def __repr__(self):
        return f'<User {self.username}>'