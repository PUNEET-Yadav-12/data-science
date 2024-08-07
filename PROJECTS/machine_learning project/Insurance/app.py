from flask import Flask, render_template, request, redirect, url_for
import joblib
from insurancedata import create_table, insert_data

# Load the model
random_forest = joblib.load('Insurance/models/randomforest.lb')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/project')
def project():
    return render_template('project.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == "POST":
        try:
            # Receive the data
            age = int(request.form['age'])
            gender = int(request.form['gender'])
            bmi = float(request.form['bmi'])
            children = int(request.form['children'])
            region = request.form['region']
            smoker = int(request.form['smoker'])
            health = int(request.form['health'])

            region_northeast = 0
            region_northwest = 0
            region_southeast = 0
            region_southwest = 0
            if region == 'se':
                region_southeast = 1
            elif region == 'sw':
                region_southwest = 1
            elif region == 'ne':
                region_northeast = 1
            else:
                region_northwest = 1

            # x_variables
            unseen_data = [[age, gender, bmi, children, smoker, health,
                            region_northeast, region_northwest, region_southeast,
                            region_southwest]]

            prediction = float(random_forest.predict(unseen_data)[0])

            data = (age, gender, bmi, children, region, smoker, health, prediction)
            insert_data(data)

            return render_template('final.html', output=prediction, age=age, gender=gender, bmi=bmi,
                                   children=children, smoker=smoker, health=health, region=region)
        except Exception as e:
            error_message = f"Error occurred: {str(e)}"
            return render_template('error.html', error_message=error_message)
    return redirect(url_for('project'))

if __name__ == "__main__":
    create_table()  # Ensure the table is created before running the app
    app.run(debug=True)
