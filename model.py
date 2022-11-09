from flask_sqlalchemy import SQLAlchemy

db= SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    email= db.Column(db.String, unique=True, nullable=False)

    def __repr__(self) -> str:
        return super().__repr__()
    
    def serialieze(self):
        return{
            "name":self.name,
            "email":self.email
        }