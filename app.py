import os

from flask import (Flask, render_template)

app = Flask(__name__)
PROJECTS = ["general", "games", "web"]

@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html', projects=PROJECTS)

@app.route('/general')
def project():
   print('Request for project page received')
   return render_template('projects/general.html', projects=PROJECTS, selected_project_name = 'general')

@app.route('/games')
def games():
   print('Request for games page received')
   return render_template('projects/games.html', projects=PROJECTS, selected_project_name = 'games')

@app.route('/web')
def web():
   print('Request for web page received')
   return render_template('projects/web.html', projects=PROJECTS, selected_project_name = 'web')

if __name__ == '__main__':
   app.run()
