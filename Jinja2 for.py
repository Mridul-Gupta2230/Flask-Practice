#HTML Integration with Python
#HTTP VERB GET AND POST
# so the very first thing is ki Home page pe show and HTML page 
# for this we will use two liberary  which is render template and request(it will help to read the posted values)
from flask import Flask,redirect, url_for, request,render_template
# render template will refer to an Html page which should be present in default file of your project folder

#more of jinja 2 template 
'''
{%...%}  statements 
{{ }} expression to print output
{# ....# } this is for comments

'''




app=Flask(__name__)

@app.route('/')
def Welcome():
    return render_template('Login.html')

@app.route('/success/<int:score>')# default wasy to create URL dynamically score is by default taken string to sccess as string we write like this
def success(score):
    res=''
    if(score>=30):
        res='PASS'
    else:
        res='FAIL'
    exp={'score': score , 'result':res}
    return render_template('Result jinja2 for.html', result = exp)

@app.route('/fail/<int:score>')# default wasy to create URL dynamically score is by default taken string to sccess as string we write like this
def fail(score):
    return (str(score))

@app.route('/result/<int:score1>')# To display result dynamicallu
def result(score1):
    b='success' if score1> 50 else 'fail'
    return redirect(url_for(b,score= score1))#the variable b will be either success or fail and will redirect to either of two function
# as we entered score1 = 11 b='fail' the url for found the dynamically called site for fail and called it to display the output

#THIS WILL BE MY RESULT CHECKER HTML PAGE
@app.route('/submit', methods=['POST','GET'])#/submit should match with action attribute in HTML form tag
def submit():
    total=0
    if(request.method=='POST'):
        science=float(request.form['science'])#the id of science tag
        maths=float(request.form['Maths'])
        C=float(request.form['C'])
        DSA=float(request.form['DSA'])
        total = (science+maths+C+DSA)/4
    RES=""
    if(total>=30):
        res="success"
    else:
        res="fail"
    return redirect(url_for(res,score= total))#this will dyanmically generate URL
if __name__=='__main__':
    app.run(debug=True)