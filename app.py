import os
from flask import Flask, render_template, request, url_for, redirect


app = Flask(__name__)

@app.route('/')
@app.route('/home')
def diary():
    # Shows the playlists
    return render_template('diary.html')


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
