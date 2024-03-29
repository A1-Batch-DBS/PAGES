from flask import Flask, render_template
#to serve a html page using flask, u need a function: render_template
#create a var..pass name of module to the class

app=Flask(__name__)
#creating a decorator
@app.route('/') #if anyone hits our websites url or ip adress i.e 127.0.0.1:5000/ then return
def home(): #function
    return render_template('login.html')

#another route
@app.route('/register') #decorator
def about():
    return render_template('register.html')

if __name__=="__main__":
    app.run(debug=True) #debug=True.. if u make changes to your code,u neednt run ur code again and again to reload on browser.
    
    #It will generate a url(127.0.0.1) where hello world will get printed. Flask is assaigned 5000
