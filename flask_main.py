from flask import Flask
from flask import render_template

from Solver import solve

app = Flask(__name__)

result = solve()

@app.route("/")
def main():
    return render_template('main.html', result=result)


@app.route('/plan')
def plan():
    return render_template('planpage.html', result=result)


@app.route('/nextSteps')
def nextSteps():
    return render_template('nextstepspage.html')


if __name__ == "__main__":
    app.run()
