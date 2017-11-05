from flask import Flask, render_template
from ParseCSV import *

app = Flask(__name__)

menu = setUpDictionary()
menu = populateMenu(menu)
menu = removeEmptyLines(menu)
date = getDay()
week = getWeek()
currentMeal = getCurrentMeal()
meals = getMeals()


@app.route('/')
def index():
    return render_template('index.html', menu=menu, date=date, week=week, currentMeal=currentMeal, meals=meals)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
