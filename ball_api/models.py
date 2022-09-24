from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Define table as class_Name(db.Model)
class Reptiles(db.Model):
    __tablename__ = "reptiles"

    id = db.Column(db.Integer, primary_key = True)
    common_name = db.Column(db.String(250))
    scientific_name = db.Column(db.String(250))
    conservation_status = db.Column(db.String(250))
    native_habitat = db.Column(db.String(500))
    fun_fact = db.Column(db.String(500))