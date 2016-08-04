from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash

from forms import BookmarkForm

app = Flask(__name__)
bookmark = []

app.config[
    'SECRET_KEY'] = "\xf8\xa3\xbb\xb0I\xc5(v\xa53\x10\x0c\xf9\xf0\x84\xf2z\xcb\x89'\x82u\x7fW"


def store_bookmark(url, description):
    bookmark.append(dict(
        url=url,
        description=description,
        user="ccrespo",
        date=datetime.utcnow()
    ))


def new_bookmarks(num):
    return sorted(bookmark, key=lambda bm: bm['date'], reverse=True)[:num]


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', new_bookmarks=new_bookmarks(5))


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = BookmarkForm()
    if form.validate_on_submit():
        url=form.url.data
        description=form.description.data
        store_bookmark(url, description)
        flash("Store '{}'".format(description))
        return redirect(url_for('index'))
    return render_template('add.html', form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 400


@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)