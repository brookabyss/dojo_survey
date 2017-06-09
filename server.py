from flask import Flask ,render_template,redirect,session,request,flash
app=Flask(__name__)
app.secret_key="12345"
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process' ,methods=['POST'])
def create_user():
    key_names=['name','location','language','comment']
    error_message="The {} field can't be empty"
    error=0
    if len(request.form['comment'])> 120:
        error+=1
        flash("Comment can't be longer than 120 characters")
    for k in key_names:

        session[k]=request.form[k]
        if len(request.form[k])<1 and k != "comment":
            error+=1
            flash(error_message.format(k))
        # print "Hello" + session['location']
    if error > 0:
        return redirect('/')
    else:
        flash("You were logged in successfully!")
        return redirect('/result')

@app.route('/result')
def show():
    return render_template('show.html')

app.run(debug=True)
