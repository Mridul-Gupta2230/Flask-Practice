from flask import Flask

#This is the WSGI application that will Communicate with the server
app=Flask(__name__)#Important to pass parameter here

#Decorator
@app.route('/')#it has two argument rule and optional where rule is basically string enclosed URL that I am going to that paticular web page
def welcome():
    return "Welcome" # Whenever User will go to @app.route('/') URL this function will be invoked automatically

@app.route('/members')
def members():#Function Name Should be different else it will give error
    return "Hey"

if __name__=='__main__':
    app.run(debug=True) # it has four arguments we usually use debug=True because while making of project if we want to make change to implement it on site without restarting the server we use debug =True
    #When You have your own Host and server you can use Host and port argument to launch it on your server
