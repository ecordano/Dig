from flask import Flask, request
from flask import render_template
from Solver import solve
from Solver import solve_man

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('main.html')


@app.route('/plan')
def plan():
    return render_template('planpage.html')


@app.route('/team')
def team():
    return render_template('team.html')


@app.route('/howItWorks')
def howItWorks():
    return render_template('howItWorks.html')


@app.route('/nextSteps')
def nextSteps():
    return render_template('nextstepspage.html')


@app.route('/results')
def results():
    return render_template('planpage.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    # do stuff
    # print request.form
    # print request.form['inputTime']
    # print float(request.form['inputTime'])
    desiredMetric = request.form['desiredBalanceMetric']
    if desiredMetric == "Personalized":
        time = float(request.form['inputTime'])
        landone = float(request.form['inputLandSun1'])
        landtwo = float(request.form['inputLandSun2'])
        landthree = float(request.form['inputLandSun3'])
        v1 = float(request.form['Cucumber'])
        v2 = float(request.form['Eggplant'])
        v3 = float(request.form['Tomato'])
        v4 = float(request.form['Green Beans'])
        v5 = float(request.form['Butternut Squash'])
        v6 = float(request.form['Cherry Tomato'])
        v7 = float(request.form['Zucchini'])
        v8 = float(request.form['Watermelon'])
        v9 = float(request.form['Bell Pepper'])
        v10 = float(request.form['Strawberries'])
        v11 = float(request.form['Potato'])
        v12 = float(request.form['Sweet Corn'])
        v13 = float(request.form['Carrots'])
        v14 = float(request.form['Beets'])
        v15 = float(request.form['Onion'])
        v16 = float(request.form['Radish'])
        v17 = float(request.form['Sweet Peas'])
        v18 = float(request.form['Lettuce'])
        v19 = float(request.form['Garlic'])
        v20 = float(request.form['Brussel Sprouts'])
        v21 = float(request.form['Kale'])
        v22 = float(request.form['Spinach'])
        result = solve_man(time, landone, landtwo, landthree, desiredMetric, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18, v19, v20, v21, v22)
        # print result
    else:
        time = float(request.form['inputTime'])
        landone = float(request.form['inputLandSun1'])
        landtwo = float(request.form['inputLandSun2'])
        landthree = float(request.form['inputLandSun3'])
        result = solve(time,landone,landtwo,landthree,desiredMetric)
        # print result

    # could do a different page to avoid the problem of planpage not rendering intially. any alternative?
    return render_template('resultspage.html', result=result)

if __name__ == "__main__":
    app.run()
