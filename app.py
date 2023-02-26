import os

import openai
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from tempfile import mkdtemp
app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        animal = request.form["animal"]
        session['paper_n'] = animal
        return redirect(url_for('suma'))
    else:
        return render_template("index.html")

@app.route("/suma", methods=("GET", "POST"))
def suma():
        paper = session.get('paper_n')
        intro_r = openai.Completion.create(
        model="text-davinci-003",
        prompt=generate_intro(paper),
        temperature=0.6,
        max_tokens=4000,
    )
        intro = intro_r.choices[0].text
        methods_r = openai.Completion.create(
        model="text-davinci-003",
        prompt=generate_methods(paper),
        temperature=0.6,
        max_tokens=4000,
    )
        methods = methods_r.choices[0].text
        results_r = openai.Completion.create(
        model="text-davinci-003",
        prompt=generate_results(paper),
        temperature=0.6,
        max_tokens=4000,
    )
        results = results_r.choices[0].text
        dis_r = openai.Completion.create(
        model="text-davinci-003",
        prompt=generate_dis(paper),
        temperature=0.6,
        max_tokens=4000,
    )
        dis = dis_r.choices[0].text
        return render_template("suma.html", intro=intro,methods=methods,results=results,dis=dis)

def generate_intro(paper):
    q = 'Summarise introduction of' + paper
    return q 
def generate_methods(paper):
    q= 'Summarise methods section with data in' + paper
    return q
def generate_results(paper):
    q = 'Summarise results in' + paper + 'with data from the paper'
    return q
def generate_dis(paper):
    q = 'Summarise discussion in' + paper
    return q