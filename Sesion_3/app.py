from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/buscar")
def buscar():
    texto = request.args.get("texto", "")
    return render_template("buscar.html", texto=texto)


@app.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        # Procesar datos enviados por el formulario
        nombre = request.form.get("nombre")
        correo = request.form.get("correo")
        return render_template(
            "registro_ok.html",
            nombre=nombre,
            correo=correo
        )
    else:
        # Mostrar el formulario vacio (GET)
        return render_template("registro.html")


@app.route("/sumar", methods=["GET", "POST"])
def sumar():
    resultado = None
    a = ""
    b = ""
    error = ""

    if request.method == "POST":
        a = request.form.get("a", "").strip()
        b = request.form.get("b", "").strip()

    if not a or not b:
        error = "Debes introducir ambos numeros."
    else:
        try:
            a_num = float(a)
            b_num = float(b)
            resultado = a_num + b_num
        except ValueError:
             error = "Debes introducir valores numericos."

    return render_template(
        "sumar.html",
                          a=a,
                          b=b,
                          resultado=resultado,
                          error=error
    )



if __name__ == "__main__":
    app.run(debug=True)