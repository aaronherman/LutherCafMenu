from flask import Flask, redirect, url_for, render_template
#from flask_sqlalchemy import SQLAlchemy
#from flask_wtf import Form


app = Flask(__name__)
#app.config['SECRET_KEY'] = 'top secret!'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://....................'


#db = SQLAlchemy(app)



###############################################




@app.route('/')
def index():
    return render_template('index.html')





if __name__ == '__main__':
    #db.create_all()
    app.run(debug=True)
