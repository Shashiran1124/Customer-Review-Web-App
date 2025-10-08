from flask import Blueprint, request, jsonify
from .models import db, Review  # Import db and Review model from models.py

app_routes = Blueprint('app_routes', __name__)

# Add a review (C)
@app_routes.route('/add_review', methods=['POST'])
def add_review():
    data = request.get_json()  # Get the data from the request
    new_review = Review(product_name=data['product_name'], review=data['review'])  # Create a new Review object
    db.session.add(new_review)  # Add the review to the session
    db.session.commit()  # Commit the transaction to the database
    return jsonify({"message": "Review added successfully!"}), 201

# Read all reviews (R)
@app_routes.route('/reviews', methods=['GET'])
def get_reviews():
    reviews = Review.query.all()
    return jsonify([review.to_dict() for review in reviews])

# Update a review (U)
@app_routes.route('/update_review/<int:id>', methods=['PUT'])
def update_review(id):
    data = request.get_json()
    review = Review.query.get(id)
    if review:
        review.review = data['review']
        db.session.commit()
        return jsonify({"message": "Review updated successfully!"})
    return jsonify({"message": "Review not found!"}), 404

# Delete a review (D)
@app_routes.route('/delete_review/<int:id>', methods=['DELETE'])
def delete_review(id):
    review = Review.query.get(id)
    if review:
        db.session.delete(review)
        db.session.commit()
        return jsonify({"message": "Review deleted successfully!"})
    return jsonify({"message": "Review not found!"}), 404
