from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(255), nullable=False)
    review = db.Column(db.Text, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "product_name": self.product_name,
            "review": self.review
        }
