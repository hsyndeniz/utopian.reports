from flask import Flask, render_template
import json
from utopian_api import Client
c = Client()

stats = c.stats
print(stats)

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html', stats = stats)


if __name__ == '__main__':
    app.run()
