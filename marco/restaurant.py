from flask import Flask, flash, render_template, request, redirect, url_for, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, Menu

app = Flask(__name__)

engine = create_engine('sqlite:///marcorestaurant.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
@app.route('/restaurants/')
def restaurantList():
    # restaurants = session.query(Restaurant).all()
    # return render_template('restaurantList.html', restaurants = restaurants)
    return "Hello Restaurant from restaurant.py"