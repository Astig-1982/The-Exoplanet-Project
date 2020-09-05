import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)


app.config["MONGODB_NAME"] =  'other_worlds'
app.config["MONGO_URI"] = 'mongodb+srv://as_cluster_2020:hello_task_boulevard@myfirstcluster.080hu.mongodb.net/other_worlds?retryWrites=true&w=majority'


mongo = PyMongo(app)


@app.route('/')
@app.route('/base')
def base():
    return render_template('base.html')



@app.route('/exoplanets_display')
def exoplanets_display():
    return render_template('exoplanets.html', exoplanets=mongo.db.exoplanets.find())


@app.route('/rocky_planets')
def rocky_planets():
    rocky_planets=mongo.db.exoplanets.find({'type': 'rocky'})
    return render_template('rocky_planets.html', rocky_planets=rocky_planets)


@app.route('/gas_giants_planets')
def gas_giants_planets():
    gas_giants_planets=mongo.db.exoplanets.find({'type': 'gas'})
    return render_template('gas_giants_planets.html', gas_giants_planets=gas_giants_planets)



@app.route('/add_favourites/<exoplanet_id>')
def add_favourites(exoplanet_id):
    favourite=mongo.db.exoplanets.find_one({"_id": ObjectId(exoplanet_id)})
    mongo.db.favourites.insert(favourite)
    return render_template('add_favourites.html', favourite_exoplanets=mongo.db.favourites.find())


@app.route('/favourite_list')
def favourite_list():
    return render_template('add_favourites.html', favourite_exoplanets=mongo.db.favourites.find())


@app.route('/delete_favourite/<exoplanet_id>')
def delete_favourite(exoplanet_id):
    mongo.db.favourites.remove({"_id": ObjectId(exoplanet_id)})
    return render_template('add_favourites.html', favourite_exoplanets=mongo.db.favourites.find())


@app.route('/detailed_exoplanet/<exoplanet_id>')
def detailed_exoplanet(exoplanet_id):
    detailed_exoplanet=mongo.db.exoplanets.find_one({"_id": ObjectId(exoplanet_id)})
    return render_template('detailed_exoplanet.html', detailed_exoplanet=detailed_exoplanet)
    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)



