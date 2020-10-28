import os
from flask import Flask, render_template, redirect, request, url_for, flash, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from os import path
if path.exists("env.py"):
  import env 

app = Flask(__name__)


app.config["MONGODB_NAME"] =  'other_worlds'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route('/base')
def base():
    return render_template('base.html')


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        #check if the username already exists in the database
        existing_user = mongo.db.users.find_one({"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists.")
            return redirect(url_for("register"))

        else:
            register = {
                "username": request.form.get("username").lower(),
                "password": generate_password_hash(request.form.get("password"))
            }
            mongo.db.users.insert_one(register)

            # put the new user into 'session' cookie
            session["user"] = request.form.get("username").lower()
            flash("Registration succesful!")
            return redirect(url_for('profile', username=session["user"])) 
    return render_template('login.html', register=True)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        existing_user = mongo.db.users.find_one({"username": request.form.get("username").lower()})

        if existing_user:
          #ensures hashed password matches user input
          if check_password_hash(existing_user["password"], request.form.get("password")):
              session["user"] = request.form.get("username").lower()
              flash("Welcome, {}".format(request.form.get("username")))
              return redirect(url_for('profile', username=session["user"]))
          else:
              #invalid password match
              flash("Incorrect Username and/or Password")
              return redirect(url_for('login'))

        else:
          #username doesn't exist
          flash("Incorrect Username and/or Password")
          return redirect(url_for('login'))
    return render_template('login.html', login=True)


@app.route('/profile/<username>', methods=['GET', 'POST'])
def profile(username):
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
        if session["user"]:
            users_list = mongo.db[username].find().count()
            users_rocky = mongo.db[username].find({'type': 'rocky'}).count()
            users_gas_giants = mongo.db[username].find({'type': 'gas giant'}).count()
            user = username.capitalize()
            return render_template('profile.html', user=user, users_list=users_list, users_rocky=users_rocky, users_gas_giants=users_gas_giants)
        else:
            return redirect(url_for('login'))


@app.route('/deleteprofile')
def deleteprofile():
    username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
    mongo.db[username].drop()
    mongo.db.users.remove({"username": session["user"]})
    session.pop('user')
    return redirect(url_for('login'))



@app.route('/logout')
def logout():
    flash('You have been logged out')
    session.pop('user')
    return redirect(url_for('login'))


@app.route('/exoplanets_display') 
def exoplanets_display():
    exoplanets=mongo.db.exoplanets.find()
    return render_template('exoplanets.html', exoplanets=exoplanets)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/small_to_large')
def small_to_large():
    sized_exoplanets=mongo.db.exoplanets.find()
    exoplanets=sorted(sized_exoplanets, key = lambda i: float(i['mass'])) 
    return render_template('exoplanets.html', exoplanets=exoplanets)


@app.route('/small_to_large_favourites')
def small_to_large_favourites():
    username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
    sized_exoplanets=mongo.db[username].find()
    favourite_exoplanets=sorted(sized_exoplanets, key = lambda i: float(i['mass'])) 
    return render_template('add_favourites.html', favourite_exoplanets=favourite_exoplanets)


@app.route('/large_to_small')
def large_to_small():
    larged_sized=mongo.db.exoplanets.find()
    exoplanets=sorted(larged_sized, key = lambda i: float(i['mass']), reverse=True) 
    return render_template('exoplanets.html', exoplanets=exoplanets)


@app.route('/large_to_small_favourites')
def large_to_small_favourites():
    username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
    larged_sized=mongo.db[username].find()
    favourite_exoplanets=sorted(larged_sized, key = lambda i: float(i['mass']), reverse=True) 
    return render_template('add_favourites.html', favourite_exoplanets=favourite_exoplanets)

 
@app.route('/rocky_planets')
def rocky_planets():
    exoplanets=mongo.db.exoplanets.find({'type': 'rocky'})
    return render_template('exoplanets.html', exoplanets=exoplanets, rocky=True)


@app.route('/gas_giants_planets')
def gas_giants_planets():
    exoplanets=mongo.db.exoplanets.find({'type': 'gas giant'})
    return render_template('exoplanets.html', exoplanets=exoplanets, gas=True)


@app.route('/favourite_list')
def favourite_list():
        try:
            username = mongo.db.users.find_one(
             {"username": session["user"]})["username"]
            return render_template('add_favourites.html', favourite_exoplanets=mongo.db[username].find())
        except:
            flash('Please login in order to access your list of favourites.')
            return redirect(url_for('login'))
        

@app.route('/add_favourites/<exoplanet_id>')
def add_favourites(exoplanet_id):
    username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
    favourite=mongo.db.exoplanets.find_one({"_id": ObjectId(exoplanet_id)})
    already_favourite=mongo.db[username].find_one({"_id": ObjectId(exoplanet_id)})
    if already_favourite:
        return render_template('already_favourite.html', favourite=favourite)
    else:
        mongo.db[username].insert(favourite)
        return redirect(url_for('favourite_list'))

        
@app.route('/delete_favourite/<exoplanet_id>')
def delete_favourite(exoplanet_id):
    username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
    mongo.db[username].remove({"_id": ObjectId(exoplanet_id)})
    return redirect(url_for('favourite_list'))


@app.route('/delete_rocky/<exoplanet_id>')
def delete_rocky(exoplanet_id):
    username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
    mongo.db[username].remove({"_id": ObjectId(exoplanet_id)})
    return redirect(url_for('favourite_rocky_planets'))


@app.route('/delete_gas_giant/<exoplanet_id>')
def delete_gas_giant(exoplanet_id):
    username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
    mongo.db[username].remove({"_id": ObjectId(exoplanet_id)})
    return redirect(url_for('favourite_gas_giants'))


@app.route('/detailed_exoplanet/<exoplanet_id>')
def detailed_exoplanet(exoplanet_id):
    detailed_exoplanet=mongo.db.exoplanets.find_one({"_id": ObjectId(exoplanet_id)})
    return render_template('detailed_exoplanet.html', detailed_exoplanet=detailed_exoplanet)


@app.route('/favourite_detailed/<exoplanet_id>')
def favourite_detailed(exoplanet_id):
    username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
    detailed_exoplanet=mongo.db[username].find_one({"_id": ObjectId(exoplanet_id)})
    return render_template('detailed_exoplanet.html', detailed_exoplanet=detailed_exoplanet)


@app.route('/favourite_rocky_planets')
def favourite_rocky_planets():
    username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
    favourite_exoplanets=mongo.db[username].find({'type': 'rocky'})
    return render_template('add_favourites.html', favourite_exoplanets=favourite_exoplanets, rocky=True)


@app.route('/favourite_gas_giants')
def favourite_gas_giants():
    username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
    favourite_exoplanets=mongo.db[username].find({'type': 'gas giant'})
    return render_template('add_favourites.html', favourite_exoplanets=favourite_exoplanets, gas=True)


@app.route('/add_exoplanet')
def add_exoplanet():
    return render_template('add_exoplanet.html')  


@app.route('/insert_exoplanet', methods=['GET', 'POST'])
def insert_exoplanet():
 if request.method == "POST":
    username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
    favourites=mongo.db[username]
    if request.form.get('type')=='rocky':
        default_image='Default-rocky'
    else:
        default_image='Default-gas'

    mass=request.form.get('mass')
    distance_from_earth=request.form.get('distance_from_earth')

    try:
        float(mass)
    except:
        wrong_data='the mass needs to be a digit'
        return render_template('wrong_data.html', wrong_data=wrong_data)
    try:
        float(distance_from_earth)
    except:
        wrong_data='distance from earth needs to be a digit'
        return render_template('wrong_data.html', wrong_data=wrong_data)

    else:
        new_planet={'planet_name': request.form.get('planet_name'),
                    'exoplanet_image': default_image,
                    'discovery_date': request.form.get('discovery_date'),
                    'distance_from_earth': request.form.get('distance_from_earth'),
                    'type': request.form.get('type'),
                    'star_system': request.form.get('star_system'),
                    'mass': request.form.get('mass'),
                    'thoughts': request.form.get('thoughts')}
        favourites.insert_one(new_planet)
        return redirect(url_for('favourite_list'))

 return redirect(url_for('add_exoplanet'))


@app.route('/mass_photo')
def mass_photo():
    return render_template('mass_photo.html')


@app.route('/calculate_weight/<exoplanet_mass>/<exoplanet_name>/<exoplanet_id>', methods=['GET', 'POST'])
def calculate_weight(exoplanet_mass, exoplanet_name, exoplanet_id):
 try:
   username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
   if request.method == 'POST':
      exoplanet=mongo.db[username].find_one({"_id": ObjectId(exoplanet_id)})
      exoplanet_weight=int(request.form.get('your_weight'))
      your_weightExoplanet = exoplanet_weight * float(exoplanet_mass)
      return render_template(
        'exoplanet_weight.html', exoplanet=exoplanet, your_weightExoplanet=your_weightExoplanet, exoplanet_name=exoplanet_name, exoplanet_id=exoplanet_id)
   else:
      detailed_exoplanet=mongo.db.exoplanets.find_one({"_id": ObjectId(exoplanet_id)})
      exoplanet=mongo.db[username].find_one({"_id": ObjectId(exoplanet_id)})
      if exoplanet:
          return render_template('calculate_weight.html', exoplanet=exoplanet)
      else:
          return render_template('not_added.html', detailed_exoplanet=detailed_exoplanet)
 except:
     flash('Please login in order to use this feature.')
     detailed_exoplanet=mongo.db.exoplanets.find_one({"_id": ObjectId(exoplanet_id)})
     return render_template('detailed_exoplanet.html', detailed_exoplanet=detailed_exoplanet)



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
