from flask_frozen import Freezer
from gh_site import app

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
