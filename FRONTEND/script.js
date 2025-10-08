document.getElementById('reviewForm').addEventListener('submit', function (event) {
    event.preventDefault();

    const productName = document.getElementById('productName').value;
    const reviewText = document.getElementById('reviewText').value;

    fetch('http://localhost:3306/add_review', {  // Make sure the backend is running on this port
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            product_name: productName,
            review: reviewText
        })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        fetchReviews();
    });
});

function fetchReviews() {
    fetch('http://localhost:3306/reviews')
        .then(response => response.json())
        .then(data => {
            const reviewsDiv = document.getElementById('reviews');
            reviewsDiv.innerHTML = '';  // Clear the previous reviews
            data.forEach(review => {
                reviewsDiv.innerHTML += `
                    <div class="review-item">
                        <strong>${review.product_name}</strong>: ${review.review}
                    </div>
                `;
            });
        });
}

// Load reviews when the page loads
fetchReviews();
