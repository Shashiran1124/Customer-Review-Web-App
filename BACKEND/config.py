from urllib.parse import quote_plus

class Config:
    # URL encode the password to handle special characters
    password = quote_plus("Shashiran@123123")  # URL-encode the password
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://root:{password}@localhost:3306/customer_db'  # Use pymysql as the connector
    SQLALCHEMY_TRACK_MODIFICATIONS = False
