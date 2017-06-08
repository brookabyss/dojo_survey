from flask import Flask ,render_template,redirect,session,request
app=Flask(__name__)
app.secret_key="12345"
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process' ,methods=['POST'])
def create_user():
    session["name"]=request.form["name"]
    session["location"]=request.form["location"]
    session["language"]=request.form["language"]
    session["location"]=request.form["location"]
    session["comment"]=request.form["comment"]
    print session["name"]
    return redirect('/result')

@app.route('/result')
def show():
    return render_template('show.html')

app.run(debug=True)
