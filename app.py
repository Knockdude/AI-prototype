from flask import Flask, render_template, request
import wikipedia

wikipedia.set_lang("es")
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def inicio():
    respuesta = ""
    if request.method == "POST":
        pregunta = request.form["pregunta"]
        try:
            respuesta = wikipedia.summary(pregunta, sentences=2)
        except:
            respuesta = "No encontré nada sobre eso."
    return render_template("index.html", respuesta=respuesta)

app.run(debug=True)