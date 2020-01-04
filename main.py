from flask import Flask, render_template
from blueprints import *

app = Flask(__name__)
app.register_blueprint(home)
app.register_blueprint(uploader)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
