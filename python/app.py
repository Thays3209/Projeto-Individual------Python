from flask import Flask, render_template, request

app = Flask(__name__, template_folder = "./src/views")

@app.route("/", methods=["GET","POST"])
def home():
      if (request.method == "GET"):
        return render_template("index.html")

      else:
            if (request.form["num1"] != "" and request.form["num2"] != ""):

                  num1 = request.form["num1"]
                  num2 = request.form["num2"]

                  if(request.form["opc"] == "soma"):
                        soma = int(num1) + int(num2)
                        return {
                              "Resultado": str(soma) 
                        } 
                  elif(request.form["opc"] == "subt"):
                        subt = int(num1) - int(num2)
                        return {
                              "Resultado": str(subt)
                        }
                  elif(request.form["opc"] == "mult"):
                        mult = int(num1) * int(num2)
                        return {
                              "Resultado": str(mult)
                        }
                  elif(request.form["opc"] == "div"):
                        div = int(num1) / int(num2)
                        return {
                              "Resultado": str(div)
                        }
            else:
                  return "informe um valor válido"
       
@app.errorhandler(404)
def not_found (error):
      return render_template("error.html")

@app.errorhandler(405)
def not_found2(error):
      return "O verbo não existe"


app.run(port=8080, debug = True)
  
