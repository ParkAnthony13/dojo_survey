import re
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "espresso"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    name_from_form = request.form['full_name']
    location_from_form = request.form['location']
    language_from_form = request.form['language']
    comments_from_form = request.form['comment']
    return render_template("show.html", name_on_template=name_from_form, location_on_template=location_from_form, language_on_template=language_from_form,comments_on_template=comments_from_form)

@app.route('/process', methods = ["POST"])
def process():
    print(request.form)
    print(request.form['full_nameCo'])
    print(request.form['coffee_today'])
    print(request.form['strengthCo'])
    print(request.form['night'])
    session['full_nameCo'] = request.form['full_nameCo']
    session['coffee_today'] = request.form['coffee_today']
    session['night'] = request.form['night']
    session['strengthCo'] = request.form['strengthCo']
    return redirect("/success")

@app.route('/success')
def save_coffee():
    print(request.form)
    return render_template(
        'success.html',
        name = session['full_nameCo'],
        coffee = session['coffee_today'],
        noCoffee = session['coffee_false'],
        strength = session['strengthCo'],
        night = session['night']
    )

if __name__=="__main__":
    app.run(debug=True)