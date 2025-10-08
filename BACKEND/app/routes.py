from flask import Blueprint, request, jsonify
from .models import db, Review  # Assuming you have a model for reviews

app_routes = Blueprint('app_routes', __name__)

# Add a review (C)
@app_routes.route('/add_review', methods=['POST'])
def add_review():
    data = request.get_json()
    new_review = Review(product_name=data['product_name'], review=data['review'])
    db.session.add(new_review)
    db.session.commit()
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
