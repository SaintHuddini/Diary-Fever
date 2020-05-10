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

# Home Route
@app.route('/')
@app.route('/home')
def diary():
    # Shows user the diaries
    return render_template('diary.html', diaries=mongo.db.diaries.find(), title='Welcome')


# New Diary Route
@app.route('/diaries/new')
def playlists_new():
    # Create a new diary
    return render_template('diaries_new.html', title='New Entry')

# Diary Submit Route
@app.route('/diaries', methods=['POST'])
def diaries_submit():
    # Submitting a new Entry
    diaries = mongo.db.diaries
    diaries.insert_one(request.form.to_dict())
    return redirect(url_for('diary'))


# Diary Show/Edit/Update/Delete Route
@app.route('/diaries/<diary_id>')
def diaries_show(diary_id):
    # Shows a single diary
    diary = mongo.db.diaries.find_one({'_id': ObjectId(diary_id)})
    return render_template('diaries_show.html', diary=diary)


@app.route('/diary_update/<diary_id>', methods=["POST"])
def diaries_update(diary_id):
    # Submit an edited Entry and update the Diary
    diaries = mongo.db.diaries
    diaries_update = ({
        'title': request.form.get('title'),
        'mood': request.form.get('mood'),
        'entry': request.form.get('entry'),
    })

    diaries.update_one(
        {'_id': ObjectId(diary_id)},
        {'$set': diaries_update})
    # take us back to the playlist's show page
    return redirect(url_for('diaries_show', diary_id=diary_id))


@app.route('/diaries_edit/<diary_id>')
def diaries_edit(diary_id):
    the_diary = mongo.db.diaries.find_one({'_id': ObjectId(diary_id)})
    all_diaries = mongo.db.diaries.find()
    return render_template('diaries_edit.html', diary=the_diary, diaries=all_diaries, title='Edit Entry')


@app.route('/diaries/<diary_id>/delete', methods=['POST'])
def diaries_delete(diary_id):
    # Delete one diary.
    diaries  = mongo.db.diaries
    diaries.delete_one({'_id': ObjectId(diary_id)})
    return redirect(url_for('diary'))


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
