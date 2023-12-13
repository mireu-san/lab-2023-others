from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(app)

# Import routes after initializing Flask app and db
from routes import *

# Initialize database tables
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
