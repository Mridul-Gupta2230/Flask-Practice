from flask import Flask


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

@app.route('/result/<int:score>')# To display result dynamicallu
def result(score):
    b='Pass' if score > 50 else 'Fail'
    return b
if __name__=='__main__':
    app.run(debug=True)
# so in above code we created three different dynamic url but what if when user entered mask and for success i want to show them different page and for fail different then 

