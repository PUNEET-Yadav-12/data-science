from flask import Flask,render_template,url_for,request


import sqlite3 
conn =  sqlite3.connect("userdata.db")

# what is decorator (@) in python?
app=Flask(__name__)
@app.route('/')# home url ( http://127.0.0.1:5000)


def home():
    return render_template('home.html')


@app.route('/about') #http://127.0.0.1:5000/about
def about():
    return render_template('about.html')

@app.route('/services') #http://127.0.0.1:5000/service
def service():
    return render_template('services.html')

@app.route('/contact') #http://127.0.0.1:5000/contact
def contact():
    return render_template('contact.html')

@app.route('/Query') #http://127.0.0.1:5000/Query
def Query():
    return render_template('Query.html')

@app.route('/user_query',methods=['GET' ,'POST']) #http://127.0.0.1:5000/user_query
def user_query():
    if request.method =="POST":
        name=request.form['name']
        age=int(request.form['age'])
        address=request.form['address']
        college=request.form['college']
        branch=request.form['branch']
        roll_no=int(request.form['roll_no'])
        query_sub=request.form['query_sub']

        user_data=[name,age,address,college,branch,roll_no,query_sub]
        return user_data
if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)
