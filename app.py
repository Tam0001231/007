from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/submit_grades", methods=["POST"])
def submit_grades():
    try:
        grade1 = int(request.form["grade1"])
        grade2 = int(request.form["grade2"])
        grade3 = int(request.form["grade3"])
        grade4 = int(request.form["grade4"])
        grade5 = int(request.form["grade5"])
        grade6 = int(request.form["grade6"])

        answer = (grade1 * 5 + grade2 * 5 + grade3 * 5 + grade4 * 5 + grade5 * 3 + grade6 * 2) / 25

        return "Your grade average is: " + str(answer)
    except ValueError:
        return "Error Occurred"

if __name__ == "__main__":
    app.run(debug=True)