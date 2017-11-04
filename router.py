from flask import Flask, render_template
from ParseCSV import *

app = Flask(__name__)

menu = setUpDictionary()
menu = populateMenu(menu)
menu = removeEmptyLines(menu)
day = getDay()

@app.route('/')
def index():
    return render_template('index.html', menu=menu, day=day)

if __name__ == '__main__':
    app.run(debug=True)
