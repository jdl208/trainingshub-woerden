from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    insertion = db.Column(db.String(50), nullable=True)
    last_name = db.Column(db.String(50), nullable=False)
    admin = db.Column(db.Boolean, default=False)

    def full_name(self):
        return (
            f"{self.first_name} {self.insertion} {self.last_name}"
            if self.insertion is not None
            else f"{self.first_name} {self.lastname}"
        )

    def hash_password(self, password):
        self.password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return self.full_name()
