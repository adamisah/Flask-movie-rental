from flask import Flask, render_template, request
import json, os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
db = SQLAlchemy(app)

migrate =Migrate(app, db)

class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    budget = db.Column(db.String(50), nullable=False)
    year = db.Column(db.String(10), nullable=False)
    cast = db.Column(db.String(100), nullable=False)
    director = db.Column(db.String(50))
    

@app.route("/")
def index():
    db = Movies.query.all()
    return render_template("index.html", movies=db)

@app.route("/new-movie", methods=['POST', 'GET'])
def new_movie():
    if request.method =='GET':
        return render_template("new_movie.html")
    else:
        # fetch movie details from request
        m = Movies()    
        m.title = request.form['title']    
        m.budget = request.form['budget']    
        m.cast = request.form['cast']    
        m.year = request.form['year']    

        db.session.add(m)
        db.session.commit()

        return render_template(
            "new_movie.html",
            success = f"Movie '{m.title}' was successfully added."
        )

@app.route("/edit/<string:title>", methods=['POST', 'GET'])
def edit_movie(title):

    m=Movies.query.filter_by(title=title).first()
    if request.method == 'GET':
        return render_template("edit.html", movie=m)
    else:
        m.title = request.form['title']
        m.title = request.form['year']
        m.title = request.form['budget']
        m.title = request.form['cast']
        
        db.session.commit()
        return render_template("edit.html",movie=m,msg=f"{m.title} successufully updated"
        )
@app.route("search")
def search():
    q = request.args.get("q")
    results = Movies.query.filter(Movies.title.contains(q)).all()

    return render_template("search.html", results = results, q=q)

@app.route("/delete/<int:id>", methods=['POST', 'GET'])
def delete(id):
    m = Movies.query.get(id)
    if m is None:
        return render_template("error.html") 

    if request.method == 'GET':
        return render_template("delete.html", movie=m)
    else:
        db.session.delete(m)
        db.session.commit()    









    return render_template("edit.html", movie = title)

@app.route("/search")
def search():
    q = Request.args.get("q")
    results = Movies.query.filter(Movies.title.contains(q).all)
    return render_template.ards.get("search.html", results = results, q=q)

    @app.route("/delete/string.title", methods=('POST', 'GET'))
    def delete_movie(title):
        m = Movies.query.filter_by(title=title).first()
        if request.method == 'POST':
            return render_template("delete.html", movie=m)
        else:
                db.session.delete(m)
                db.session.commit()
                return redirect("/")
              