from flask import Flask 
from flask import render_template
from flask import request


app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def home():
  if request.method == "POST":
    val1 = int(request.form["campo1"])

    if (request.form.get("calcular")):
      res = val1 ** 2 
      return render_template('index.html', val=res)

    return render_template('index.html')
  else:
    return render_template('index.html', val="nada")

app.run(host="0.0.0.0", debug=True)