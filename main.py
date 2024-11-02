from flask import Flask,redirect,url_for,render_template,request
app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')


@app.route('/pas/<int:number>')
def pas(number):
    res = ""
    if number <33:
        res = 'fail'
    else:
        res = 'pas'
    return render_template('result.html',result = res)


@app.route('/fail/<int:number>')
def fail(number):
    return 'you are fail'+str(number)



@app.route('/result/<int:marks>')
def result(marks):
    result = ""
    if marks <33:
        result = 'fail'
    else:
        result = 'pas'

    return redirect(url_for(result,number =marks))
 
@app.route('/submit',methods = ['POST','GET'])
def submit():
    total_score=0
    if request.method == 'POST':
       science =float(request.form['science'])
       maths=float(request.form['maths']) 
       c=float(request.form['c']) 
       python=float(request.form['python']) 
       total_score=(science+maths+c+python)/4
   
    return redirect(url_for('pas',number= total_score))


if __name__=='__main__':
    app.run(debug = True)
