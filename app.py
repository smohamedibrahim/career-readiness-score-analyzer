from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def home():
    return open("index.html").read()
@app.route('/calculate', methods=['POST'])
def calculate():
    name = request.form['name']
    skills = int(request.form['skills'])
    projects = int(request.form['projects'])
    certifications = int(request.form['certifications'])
    cgpa = float(request.form['cgpa'])
    score = 0
    score += min(skills * 4, 40)
    score += min(projects * 5, 25)
    score += min(certifications * 4, 20)
    score += min((cgpa / 10) * 15, 15)
    if score <= 40:
        level = "Beginner"
    elif score <= 70:
        level = "Intermediate"
    else:
        level = "Job Ready"
    return render_template(
        "result.html",
        name=name,
        score=round(score, 2),
        level=level
    )
if __name__ == '__main__':
    app.run(debug=True)
