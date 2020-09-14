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


@app.route('/home')
def home():
    return render_template('home.html')



@app.route('/exoplanets_display')
def exoplanets_display():
    return render_template('exoplanets.html', exoplanets=mongo.db.exoplanets.find())


@app.route('/rocky_planets')
def rocky_planets():
    rocky_planets=mongo.db.exoplanets.find({'type': 'rocky'})
    return render_template('rocky_planets.html', rocky_planets=rocky_planets)


@app.route('/gas_giants_planets')
def gas_giants_planets():
    gas_giants_planets=mongo.db.exoplanets.find({'type': 'gas giant'})
    return render_template('gas_giants_planets.html', gas_giants_planets=gas_giants_planets)



@app.route('/add_favourites/<exoplanet_id>')
def add_favourites(exoplanet_id):
    favourite=mongo.db.exoplanets.find_one({"_id": ObjectId(exoplanet_id)})
    already_favourite=mongo.db.favourites.find_one({"_id": ObjectId(exoplanet_id)})
    if already_favourite:
        return render_template('already_favourite.html', favourite=favourite)
    else:
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


@app.route('/favourite_rocky_planets')
def favourite_rocky_planets():
    rocky_planets=mongo.db.favourites.find({'type': 'rocky'})
    return render_template('favourite_rocky_planets.html', rocky_planets=rocky_planets)


@app.route('/favourite_gas_giants')
def favourite_gas_giants():
    gas_giants_planets=mongo.db.favourites.find({'type': 'gas giant'})
    return render_template('favourite_gas_giants.html', gas_giants_planets=gas_giants_planets)


@app.route('/add_exoplanet')
def add_exoplanet():
    return render_template('add_exoplanet.html')  


@app.route('/insert_exoplanet', methods=['POST'])
def insert_exoplanet():
    favourites=mongo.db.favourites
    new_planet={'planet_name': request.form.get('planet_name'),
                'discovery_date': request.form.get('discovery_date'),
                'distance_from_earth': request.form.get('distance_from_earth'),
                'type': request.form.get('type'),
                'star_system': request.form.get('star_system'),
                'mass': request.form.get('mass'),
                'thoughts': request.form.get('thoughts')}
    favourites.insert_one(new_planet)
    return redirect(url_for('favourite_list'))


@app.route('/calculate_weight/<exoplanet_id>')
def calculate_weight(exoplanet_id):
    detailed_exoplanet=mongo.db.exoplanets.find_one({"_id": ObjectId(exoplanet_id)})
    exoplanet=mongo.db.favourites.find_one({"_id": ObjectId(exoplanet_id)})
    if exoplanet:
        return render_template('calculate_weight.html', exoplanet=exoplanet)
    else:
        return render_template('not_added.html', detailed_exoplanet=detailed_exoplanet)


@app.route('/calculate/<exoplanet_mass>/<exoplanet_name>', methods=['POST'])
def calculate(exoplanet_mass, exoplanet_name):
    exoplanet_weight=int(request.form.get('your_weight'))
    your_weightExoplanet = exoplanet_weight * float(exoplanet_mass)
    return render_template('exoplanet_weight.html', your_weightExoplanet=your_weightExoplanet, exoplanet_name=exoplanet_name)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)




