from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods = ['GET','POST'])
def index():
    bmi = ''
    bmi_category = ''
    if request.method =='POST' and 'weight' in request.form:
        weight = float(request.form.get('weight'))
        height =float(request.form.get('height'))
        bmi  = calc_bmi(weight, height)
        bmi_category = get_bmi_category(bmi)

    return render_template("index.html",
                           bmi = bmi,
                           bmi_category = bmi_category)


def calc_bmi (weight, height):
    return round(weight / ((height / 100) **2), 2)


def get_bmi_category(bmi):
    if bmi < 18.5:
        return 'Under weight'
    elif 18.5 <= bmi <= 24.9:
        return 'Healthy weight'
    elif 24.9 <= bmi <= 29.9:
        return 'Over weight'
    else:
        return 'Obesity'
    


if __name__ == "__main__":
    app.run()
