import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)


app.config["MONGODB_NAME"] =  'other_worlds'
app.config["MONGO_URI"] = 'mongodb+srv://as_cluster_2020:hello_task_boulevard@myfirstcluster.080hu.mongodb.net/other_worlds?retryWrites=true&w=majority'


mongo = PyMongo(app)


@app.route('/')
@app.route('/exoplanets_display')
def exoplanets_display():
    return render_template('exoplanets.html', exoplanets=mongo.db.exoplanets.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)



