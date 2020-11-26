import os
from flask import Flask, render_template, redirect, request, url_for, flash, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from os import path
if path.exists("env.py"):
  import env 

app = Flask(__name__)


app.config["MONGODB_NAME"] = 'other_worlds'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route('/')
def home():
    return render_template('pages/home.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    displaying the register page
    """
    if request.method == "POST":
        """
        check if the username already exists in the database
        """
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists.")
            return redirect(url_for('register'))

        else:
            register = {
                "username": request.form.get("username").lower(),
                "password": generate_password_hash(
                    request.form.get("password"))
            }
            mongo.db.users.insert_one(register)
            session["user"] = request.form.get("username").lower()
            flash("Registration succesful!")
            return redirect(url_for('profile', username=session["user"]))
    return render_template('pages/login.html', register=True)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    displaying the login page
    """
    if request.method == "POST":
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
          """
          if the user exists
          """
          if check_password_hash(
                  existing_user["password"], request.form.get("password")):
              session["user"] = request.form.get("username").lower()
              flash("Welcome, {}".format(request.form.get("username")))
              return redirect(url_for('profile', username=session["user"]))
          else:
              flash('Incorrect Username and/or Password')
              return redirect(url_for('login'))

        else:
          """
          if the user doesn't exists
          """
          flash('Incorrect Username and/or Password')
          return redirect(url_for('login'))
    return render_template('pages/login.html', login=True)


@app.route('/profile/<username>', methods=['GET', 'POST'])
def profile(username):
        """
        displaying the user's profile
        """
        users_list = mongo.db[username].find().count()
        users_rocky = mongo.db[username].find(
            {'type': 'rocky'}).count()
        users_gas_giants = mongo.db[username].find(
            {'type': 'gas giant'}).count()
        user = username.capitalize()
        return render_template('pages/profile.html', user=user,
                users_list=users_list, users_rocky=users_rocky,
                        users_gas_giants=users_gas_giants)


@app.route('/delete/profile')
def deleteprofile():
    """
    delete the user's profile
    """
    username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]

    """
    delete the users favourites list
    """
    mongo.db[username].drop()

    mongo.db.users.remove({"username": session["user"]})
    session.pop('user')
    flash("Profile deleted! Hope to see you back soon, {}.".format(username.capitalize()))
    return redirect(url_for('register'))


@app.route('/logout')
def logout():
    """
    user log out
    """
    flash('You have been logged out')
    session.pop('user')
    return redirect(url_for('login'))


@app.route('/display/exoplanets')
def exoplanets_display():
    """
    display the main list of exoplanets
    """
    exoplanets = mongo.db.exoplanets.find()
    return render_template('pages/exoplanets.html', exoplanets=exoplanets)


@app.route('/about')
def about():
    """
    displaying the about page
    """
    return render_template('pages/about.html')


@app.route('/small/to/large')
def small_to_large():
    """
    displaying exoplanets from smallest mass to largest mass
    """
    sized_exoplanets = mongo.db.exoplanets.find()
    exoplanets = sorted(sized_exoplanets, key = lambda i: float(i['mass']))
    return render_template('pages/exoplanets.html', exoplanets=exoplanets)


@app.route('/favourites/exoplanets/small/to/large')
def small_to_large_favourites():
    """
    displaying exoplanets from user's
    favourits list from
    smallest mass to largest mass
    """
    username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
    sized_exoplanets = mongo.db[username].find()
    favourite_exoplanets = sorted(sized_exoplanets,
                         key = lambda i: float(i['mass']))
    return render_template('pages/favourites.html',
           favourite_exoplanets=favourite_exoplanets)


@app.route('/large/to/small')
def large_to_small():
    """
    displaying exoplanets from largest mass to smallest mass
    """
    larged_sized = mongo.db.exoplanets.find()
    exoplanets = sorted(larged_sized,
                     key = lambda i: float(
                         i['mass']), reverse=True)
    return render_template('pages/exoplanets.html', exoplanets=exoplanets)


@app.route('/favourites/exoplanets/large/to/small')
def large_to_small_favourites():
    """
    displaying exoplanets from user's list from largest mass to smallest mass
    """
    username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
    larged_sized = mongo.db[username].find()
    favourite_exoplanets = sorted(larged_sized,
                                key = lambda i: float(
                                    i['mass']), reverse=True)
    return render_template('pages/favourites.html',
           favourite_exoplanets=favourite_exoplanets)


@app.route('/rocky/planets')
def rocky_planets():
    """
    displaying only the rocky
    planets from the main list of exoplanets
    """
    exoplanets = mongo.db.exoplanets.find(
        {'type': 'rocky'})
    return render_template('pages/exoplanets.html',
           exoplanets = exoplanets, rocky=True)


@app.route('/gas/planets')
def gas_giants_planets():
    """
    displaying only the gas
    giants from the main list of exoplanets
    """
    exoplanets = mongo.db.exoplanets.find(
        {'type': 'gas giant'})
    return render_template('pages/exoplanets.html',
           exoplanets=exoplanets, gas=True)


@app.route('/favourites/list')
def favourite_list():
        """
        displaying the user's favourites list
        """
        try:
            username = mongo.db.users.find_one(
             {"username": session["user"]})["username"]
        except Exception:
            flash('Please login in order to access your list of favourites.')
            return redirect(url_for('login'))
        return render_template('pages/favourites.html',
                favourite_exoplanets=mongo.db[username].find())


@app.route('/favourite/<exoplanet_id>')
def favourite(exoplanet_id):
        """
        add an exoplanet from the main list
        to the user's list of favourites
        """
        try:
            username = mongo.db.users.find_one(
                {"username": session["user"]})["username"]
            favourite = mongo.db.exoplanets.find_one(
                {"_id": ObjectId(exoplanet_id)})
        except Exception:
            flash('Please log in in order to add any exoplanet to your list of favourites')
            return redirect(url_for('login'))
        """
        check if the exoplanet is already in the user's favourites list
        """
        already_favourite = mongo.db[username].find_one(
            {"_id": ObjectId(exoplanet_id)})
        if already_favourite:
            return render_template('pages/alreadyFavourite.html',
                      favourite=favourite)
        else:
            mongo.db[username].insert(favourite)
            return redirect(url_for('favourite_list'))


@app.route('/delete/favourite/<exoplanet_id>')
def delete_favourite(exoplanet_id):
    """
    delete an exoplanet from the user's
    list of favourites
    """
    username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
    mongo.db[username].remove({"_id": ObjectId(exoplanet_id)})
    return redirect(url_for('favourite_list'))


@app.route('/delete/rocky/exoplanet/<exoplanet_id>')
def delete_rocky(exoplanet_id):
    """
    delete an exoplanet from the favourite rocky worlds
    page and returning on the same page after
    """
    username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
    mongo.db[username].remove({"_id": ObjectId(exoplanet_id)})
    return redirect(url_for('favourite_rocky_planets'))


@app.route('/delete/gas/exoplanet/<exoplanet_id>')
def delete_gas_exoplanet(exoplanet_id):
    """
    delete an exoplanet from the favourite gas giants
    page and returning on the same page after
    """
    username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
    mongo.db[username].remove({"_id": ObjectId(exoplanet_id)})
    return redirect(url_for('favourite_gas_giants'))


@app.route('/detailed/exoplanet/<exoplanet_id>')
def detailed_exoplanet(exoplanet_id):
    """
    displaying exoplanet in detail
    """
    detailed_exoplanet = mongo.db.exoplanets.find_one(
        {"_id": ObjectId(exoplanet_id)})
    return render_template('pages/detailedExoplanet.html',
           detailed_exoplanet=detailed_exoplanet)


@app.route('/detailed/favourite/exoplanet/<exoplanet_id>')
def favourite_detailed(exoplanet_id):
    """
    displaying exoplanet from user's
    favourites list in detail
    """
    username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
    detailed_exoplanet = mongo.db[username].find_one(
        {"_id": ObjectId(exoplanet_id)})
    return render_template('pages/detailedExoplanet.html',
           detailed_exoplanet=detailed_exoplanet)


@app.route('/favourite/rocky/planets')
def favourite_rocky_planets():
    """
    displaying only the rocky planets from user's favourites list
    """
    username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]

    favourite_exoplanets = mongo.db[username].find(
        {'type': 'rocky'})
    return render_template('pages/favourites.html',
           favourite_exoplanets=favourite_exoplanets, rocky=True)


@app.route('/favourite/gas/giants')
def favourite_gas_giants():
    """
    displaying only the gas giants from user's favourites list
    """
    username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]

    favourite_exoplanets = mongo.db[username].find(
        {'type': 'gas giant'})
    return render_template('pages/favourites.html',
           favourite_exoplanets=favourite_exoplanets, gas=True)


@app.route('/insert/exoplanet', methods=['GET', 'POST'])
def insert_exoplanet():
 """
 inserting an exoplanet into user's favourites list
 with different default image, depending on the type
 of exoplanet inserted
 """
 if request.method == "POST":
    try:
        username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
    except Exception:
        flash("Please log in in order to add an exoplanet to your favourites list")
        return redirect(url_for('login'))

    favourites = mongo.db[username]

    if request.form.get('type') == 'rocky':
        default_image = 'Default-rocky'
    else:
        default_image = 'Default-gas'

    new_planet = {'planet_name': request.form.get('planet_name'),
                    'exoplanet_image': default_image,
                    'discovery_date': request.form.get('discovery_date'),
                    'distance_from_earth': float(request.form.get(
                        'distance_from_earth')),
                    'type': request.form.get('type'),
                    'star_system': request.form.get('star_system'),
                    'mass': float(request.form.get('mass'))}
    favourites.insert_one(new_planet)
    return redirect(url_for('favourite_list'))
 return render_template('pages/addExoplanet.html')


@app.route('/mass/location/photo')
def mass_photo():
    """
    displaying an image with the location
    on wikipedia of the exoplanet's mass property
    """
    return render_template('pages/massPhoto.html')


@app.route('/calculate/your/weight/<exoplanet_mass>/<exoplanet_name>/<exoplanet_id>',
             methods=['GET', 'POST'])
def calculate_weight(exoplanet_mass, exoplanet_name, exoplanet_id):
 """
 calculate the user's weight on exoplanet
 """
 try:
   username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
 except Exception:
     flash('Please login in order to use this feature.')
     return redirect(url_for('login'))

 if request.method == 'POST':
      exoplanet = mongo.db[username].find_one(
          {"_id": ObjectId(exoplanet_id)})

      your_weight = int(request.form.get('your_weight'))
      your_weightExoplanet = round(your_weight * float(exoplanet_mass), 2)

      return render_template(
        'pages/exoplanetWeight.html', exoplanet=exoplanet,
        your_weightExoplanet=your_weightExoplanet,
        exoplanet_name=exoplanet_name, exoplanet_id=exoplanet_id)

 else:
      detailed_exoplanet=mongo.db.exoplanets.find_one({"_id": ObjectId(exoplanet_id)})
      exoplanet=mongo.db[username].find_one({"_id": ObjectId(exoplanet_id)})
      if exoplanet:
          """
          check if the exoplanet is added to the user's 
          favourites list
          """
          return render_template('pages/calculateWeight.html', exoplanet=exoplanet)
      else:
          return render_template(
              'pages/notAdded.html', detailed_exoplanet=detailed_exoplanet)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('pages/404NotFound.html'), 404


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=os.environ.get('DEBUG'))
