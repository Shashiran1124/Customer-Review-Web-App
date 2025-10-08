from datetime import datetime
from . import db  # Import db from __init__.py

class Review(db.Model):
    __tablename__ = 'reviews'  # Table name in MySQL

    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(255), nullable=False)
    review = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'product_name': self.product_name,
            'review': self.review,
            'created_at': self.created_at
        }
