from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint

app = Flask(__name__)

# DB CONNECTION 
# app.config['SQLALCHEMY_DATABASE_URI']= 'mysql://username:password@service_name/database_name'
app.config['SQLALCHEMY_DATABASE_URI']= 'mysql://admin:admin@db/main'
CORS(app)

db =SQLAlchemy(app)

# PRODUCT WILL BE CREATED IN DJANGO APP  - 
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))

class productUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)

    UniqueConstraint('user_id', "product_id", name="user_product_unique")
    

@app.route('/')
def index():
    return "Hello WOrld"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')