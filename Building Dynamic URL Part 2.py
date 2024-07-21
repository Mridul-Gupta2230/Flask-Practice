from flask import Flask,redirect, url_for

#redirect is used to redirect user to a different page 
#url_for tell which ur;l to go to



app=Flask(__name__)

@app.route('/')
def Welcome():
    return "HEy"

@app.route('/success/<int:score>')# default wasy to create URL dynamically score is by default taken string to sccess as string we write like this
def success(score):
    return (str(score))

@app.route('/fail/<int:score>')# default wasy to create URL dynamically score is by default taken string to sccess as string we write like this
def fail(score):
    return (str(score))

@app.route('/result/<int:score1>')# To display result dynamicallu
def result(score1):
    b='success' if score1> 50 else 'fail'
    return redirect(url_for(b,score= score1))#the variable b will be either success or fail and will redirect to either of two function
# as we entered score1 = 11 b='fail' the url for found the dynamically called site for fail and called it to display the output
if __name__=='__main__':
    app.run(debug=True)