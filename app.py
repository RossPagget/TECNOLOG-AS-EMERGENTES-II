from flask import Flask, render_template, request
 
app = Flask(__name__)
 
@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("form.html")
 
@app.route("/saludo", methods=["POST"])
def saludo():
    nombre = request.form.get("nombre", "").strip()
    return render_template("saludo.html", nombre=nombre)
 
if __name__ == "__main__":
    app.run(debug=True)