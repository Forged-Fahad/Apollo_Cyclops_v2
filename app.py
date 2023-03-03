from flask import Flask, render_template
app = Flask(__name__)

PLANETS = [
  {
    'id': 1,
    "name" : "55 Canceri E",
    "galaxy" : "Milky Way",
    "distance" : "40 light years"
  },
  {
    'id': 2,
    "name" : "TOI 700",
    "galaxy" : "Messier 51",
    "distance" : "100 light years"
  },
  {
    'id': 3,
    "name" : "PA-99-N2",
    "galaxy" : "Andromeda",
    "distance" : "2,185,247 light years"
  },
  {
    'id': 4,
    "name" : "Kepler 452b",
    "galaxy" : "Milky Way",
    "distance" : "1150 light years"
  }
]
@app.route("/")
def hello_world():
  return render_template("index.html" , planets = PLANETS)

if __name__ == "__main__":
  app.run(host = "0.0.0.0", debug = True )