from wolfbot import app, db
from flask import render_template, redirect, url_for

class GameStats(db.Model):
    __tablename__ = "gamestats"
    size = db.Column(db.Integer, primary_key=True)
    villagewins = db.Column(db.Integer)
    wolfwins = db.Column(db.Integer)
    totalgames = db.Column(db.Integer)

class Roles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.Text(255))

class RoleStats(db.Model):
    __tablename__ = "rolestats"
    player = db.Column(db.Text(255), primary_key=True)
    role = db.Column(db.Text(255), primary_key=True)
    teamwins = db.Column(db.Integer)
    individualwins = db.Column(db.Integer)
    totalgames = db.Column(db.Integer)

@app.route("/")
def index():
  players = db.session.query(RoleStats.player).distinct()
  return render_template("index.html", players=players)

@app.route("/play")
def play():
  return render_template("play.html")

@app.route("/stats")
def stats():
  rolestats = GameStats.query.order_by(GameStats.size).all()
  return render_template("stats.html", stats=rolestats)

@app.route("/player/<username>")
def player(username):
  stats = RoleStats.query.filter_by(player=username).all()
  if not stats:
    return redirect(url_for("index"))
  return render_template("playerstats.html", stats=stats, username=username)

@app.route("/style")
def style():
  return render_template("style.html")

@app.route("/roles")
def roles():
  return render_template("roles.html")


