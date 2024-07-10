#!/usr/bin/python3

from flask import Flask, redirect, url_for
from setup import create_app, db
from models.user import User
from models.city import City
from models.country import Country
from models.amenity import Amenity
from models.place import Place
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app, db = create_app()


from data_manager import DataManager
data_manager = DataManager()


admin = Admin(app, name='My App', template_mode='bootstrap3')

# Add your models to Flask-Admin
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(City, db.session))
admin.add_view(ModelView(Country, db.session))
admin.add_view(ModelView(Amenity, db.session))
admin.add_view(ModelView(Place, db.session))

# Routes for home and managing users 
@app.route('/')
def index():
    return redirect(url_for('admin.index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("Database tables created successfully.")
    app.run(debug=True, port=5000)
