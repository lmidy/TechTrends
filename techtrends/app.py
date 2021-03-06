import sqlite3
import sys

from flask import Flask, jsonify, json, render_template, request, url_for, redirect, flash
from werkzeug.exceptions import abort
import logging

# variable for count of all db connections
connection_count = 0


# Function to get a database connection.
# This function connects to database with the name `database.db`, increments count for each connection
def get_db_connection():
    global connection_count
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row
    connection_count += 1
    return connection


# Function to get a post using its ID
def get_post(post_id):
    connection = get_db_connection()
    post = connection.execute('SELECT * FROM posts WHERE id = ?',
                              (post_id,)).fetchone()
    connection.close()
    return post


# Define the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'


# Define the main route of the web application
@app.route('/')
def index():
    connection = get_db_connection()
    posts = connection.execute('SELECT * FROM posts').fetchall()
    connection.close()
    return render_template('index.html', posts=posts)


# Define how each individual article is rendered
# If the post ID is not found a 404 page is shown
@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    if post is None:
        app.logger.error('Article with id %s is non existent!', post_id)
        return render_template('404.html'), 404
    else:
        app.logger.info('Article "{title}" retrieved!'.format(title=post['title']))
        return render_template('post.html', post=post)


# Define the About Us page
@app.route('/about')
def about():
    app.logger.info('About Us page retrieved!')
    return render_template('about.html')


# Define the post creation functionality
@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            connection = get_db_connection()
            connection.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                               (title, content))
            connection.commit()
            connection.close()
            app.logger.info('Article "{title}" created!'.format(title=title))
            return redirect(url_for('index'))

    return render_template('create.html')


# define the healthz endpoint to return the status of the application
@app.route('/healthz')
def health():
    try:
        connection = get_db_connection()
        connection.execute('SELECT * FROM posts').fetchall()
        connection.close()
        return {'result': 'OK - healthy'}, 200
    except Exception:
        app.logger.exception('Hitting healthz endpoint unavailable')
        return {'result': 'NOT OK - unhealthy'}, 500


# define a metrics endpoint that returns counts of posts in database and counts of connections to db
@app.route('/metrics')
def metrics():
    connection = get_db_connection()
    posts = connection.execute('SELECT * FROM posts').fetchall()
    connection.close()
    post_count = len(posts)
    data = {"db_connection_count": connection_count, "post_count": post_count}
    app.logger.info('Metrics requests successful')
    return data


# start the application on port 3111
if __name__ == "__main__":
    logging.basicConfig(
        format='%(levelname)s:%(name)s:%(asctime)s, %(message)s',
        datefmt='%m/%d/%Y, %I:%M:%S', level=logging.DEBUG)
    app.run(host='0.0.0.0', port='3111')
