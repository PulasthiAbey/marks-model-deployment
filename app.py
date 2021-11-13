from flask import Flask, render_template, request
import marks as m

app = Flask(__name__)

@app.route("/", methods = ["POST"])
def handleMain():
    if request.method=="POST":
        hrs = request.form['hrs']
        marks_predicted = m.marks_prediction(hrs)
        mk = marks_predicted
    
    return render_template("index.html", my_marks = mk)

# @app.route("/sub", methods=["POST"])
# def submit():
#     # HTML --> Py transmission
#     if request.method == "POST":
#         name = request.form["hrs"] 
    
#     # .py --> HTML transmission
#     return render_template("sub.html", n = name)

if __name__ == "__main__":
    app.run(debug=True)