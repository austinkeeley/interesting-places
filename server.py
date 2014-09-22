"""
Development server for interesting places
"""

from places import app

if __name__ == '__main__':
    print 'Interesting Places'
    app.run(debug=True)
