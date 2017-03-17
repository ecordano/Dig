from flask import Flask, request
from flask import render_template
from Solver import solve

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('main.html')


@app.route('/plan')
def plan():
    return render_template('planpage.html')


@app.route('/nextSteps')
def nextSteps():
    return render_template('nextstepspage.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    # do stuff
    print request.form
    # print request.form['inputTime']
    # print float(request.form['inputTime'])
    time = float(request.form['inputTime'])
    landone = float(request.form['inputLandSun1'])
    landtwo = float(request.form['inputLandSun2'])
    landthree = float(request.form['inputLandSun3'])
    result = solve(time,landone,landtwo,landthree)
    print result

    # could do a different page to avoid the problem of planpage not rendering intially. any alternative?
    return render_template('planpage.html', result=result)

if __name__ == "__main__":
    app.run()
