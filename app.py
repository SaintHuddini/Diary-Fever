import os
from flask import Flask, render_template, request, url_for, redirect
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
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
    # Shows user the diaries
    return render_template('diary.html', diaries=mongo.db.diaries.find())


@app.route('/diaries/new')
def playlists_new():
    # Create a new diary
    return render_template('diaries_new.html')


@app.route('/diaries', methods=['POST'])
def diaries_submit():
    # Submitting a new Entry
    diaries = mongo.db.diaries
    diaries.insert_one(request.form.to_dict())
    return redirect(url_for('diary'))


@app.route('/diaries/<diary_id>')
def diaries_show(diary_id):
    # Shows a single diary
    diary = mongo.db.diaries.find_one({'_id': ObjectId(diary_id)})
    return render_template('diaries_show.html', diary=diary)






if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
