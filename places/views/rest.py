"""
REST endpoints
"""

from places import app

@app.route('/')
def index():
    return 'interesting places'

@app.route('/place', methods=['POST'])
def add_place(place):
    pass
