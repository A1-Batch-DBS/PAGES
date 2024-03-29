from flask import Flask, render_template, request, redirect,session
import mysql.connector
import os


#to serve a html page using flask, u need a function: render_template
#create a var..pass name of module to the class
#session is a type of dictionary
#session used so that user cant enter home without login and login page shld not have login details. user shldnt be directly able to go to home w/o login
#create a connection object conn

conn=mysql.connector.connect(user='root',password='Tjss@2020',host='localhost',database='Library')
#cursor-used to communicate with database
cursor=conn.cursor()

app=Flask(__name__)
app.secret_key=os.urandom(24)


#creating a decorator
@app.route('/') #if anyone heyJzdHVkZW50X0lkIjoiUzAxIn0.Zgcfvw.dB1fj3xVGmGd6piWgx5o49Ua_wwits our websites url or ip adress i.e 127.0.0.1:5000/ then return
def login(): #function
    return render_template('login.html')

#another route
@app.route('/register') #decorator
def about():
    return render_template('register.html')

#user enters home after login
@app.route('/home')
def home():
    if 'student_id' in session: #this will be true only if user has logged in
        return render_template('home.html')
    else:
        return redirect('/') #not registered student will be redirected the login page
    #return render_template('home.html')

#when u send data from filling html forms to server->data travels through post method
#when u send data through url -> get method
#form->post method
#url->get method

@app.route('/login_validation',methods=['POST']) # to receive data coming through post,methods=['POST']
def login_validation():
    name=request.form.get('uname')
    email=request.form.get('uemail')
    password=request.form.get('upassword')

    cursor.execute("""SELECT * FROM `student` WHERE `Email` LIKE '{}' and `password` LIKE '{}'""".format(email,password))
    #return """SELECT * FROM `student` WHERE `email` LIKE {} AND `password` LIKE {}""".format(email,password)
    students=cursor.fetchall()
    print(students)
    #return "Hello motherfucker"

    if len(students)>0:
        session['student_id']=students[0][0]
        return redirect('/home')
        #return render_template('home.html')
    else:
        return redirect('/')
        #return render_template('login.html')

# [(),(),()]  --> List of tuples

#adding new registrations into the dats=base
@app.route('/add_student',methods=['POST'])
def add_student():
    name=request.form.get('username')
    email=request.form.get('useremail')
    password=request.form.get('userpassword')
    city=request.form.get('city')
    state=request.form.get('state')
    zip=request.form.get('zip')
    id=request.form.get('id')
    college=request.form.get('college')
    
    cursor.execute("""INSERT INTO `student` (`StudentId`,`Student_Name`,`State`,`City`,`ZipCode`,`Email`,`College`,`password`) 
                   VALUES('{}','{}','{}','{}','{}','{}','{}','{}')""".format(id,name,state,city,zip,email,college,password))
    conn.commit()

    cursor.execute("""SELECT * FROM `student` WHERE `Email` LIKE '{}'""".format(email))
    myuser=cursor.fetchall()
    session['student_id']=myuser[0][0]
    return redirect("/home")

    #return "Omg congratulations .Student registered successfully"
    #return "..."


#logout
@app.route('/logout')
def logout():
    session.pop('student_id')
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True) #debug=True.. if u make changes to your code,u neednt run ur code again and again to reload on browser.
    
    #It will generate a url(127.0.0.1) where hello world will get printed. Flask is assaigned 5000
