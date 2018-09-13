from flask import Flask, flash, render_template, request, redirect, url_for, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, Menu

app = Flask(__name__)

engine = create_engine('sqlite:///marcorestaurant.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# ===============================  Restaurant ================================= #
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/restaurants/')
def restaurantsList():
    restaurants = session.query(Restaurant).all()
    return render_template('restaurantlist.html', restaurants = restaurants )
   

# ===============================  Menu ================================= #
@app.route('/Menu')
def menuList():
    # restaurants = session.query(Restaurant).all()
    return render_template('menu.html')



if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
