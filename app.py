import os
from flask import Flask, render_template, request, url_for, redirect


app = Flask(__name__)


diarys = [
    { 'title': 'Hello world!', 'mood': 'happy', 'entry': 'A new day and a new beginning.'},
    { 'title': 'A buggy day', 'mood': 'tired', 'entry': 'Full of bugs and roadblocks.'}
]


@app.route('/')
@app.route('/home')
def diary():
    # Shows user the diary
    return render_template('diary.html', diarys=diarys)


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
