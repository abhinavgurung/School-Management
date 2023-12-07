from app import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), index=True, nullable=False)

    def __repr__(self):
        return f"<id = ${self.id} , name= ${self.name}>"