from flask import Flask, render_template
app = Flask (__name__)

@app.route('/')
def level_one():
    return render_template("index.html", row = 8, column = 8)
@app.route('/<int:num1>')
def row(num1):
    return render_template("index.html", row = num1)
@app.route('/<int:num1>/<int:num2>')
def column(num1, num2):
    return render_template("index.html", row = num1, column = num2) 
# @app.route('/<int:num1>/<int:num2>/<string:color1>/<string:color2>')
# def level_three(num1, num2, one, two):
#     return render_template("index.html", row = num1, column = num2, color1 = one, color2 = two )

if __name__ == "__main__":
    app.run(debug = True)