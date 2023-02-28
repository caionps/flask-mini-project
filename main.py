from flask import Flask 
from flask import render_template
from flask import request


app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def home():
  if request.method == "POST":
    aresta = int(request.form["campo1"])
    
    if (request.form.get("calcular")):
      resultado = aresta ^ 2
      return render_template('index.html', area=resultado)
      
    return render_template('index.html')
    
  else:
    return render_template('index.html', area='na')

app.run(host="0.0.0.0", debug=True)