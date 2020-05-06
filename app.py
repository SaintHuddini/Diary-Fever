import os
from flask import Flask, render_template, request, url_for, redirect
from flask_pymongo import PyMongo
import env


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'DiaryDB'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')
mongo = PyMongo(app)

print(os.getenv('MONGO_URI', 'mongodb://localhost'))
app.secret_key = "secretkey"


@app.route('/')
@app.route('/home')
def diary():
    # Shows user the diary
    return render_template('diary.html', diaries=mongo.db.diaries.find())


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
