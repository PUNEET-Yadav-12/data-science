from flask import Flask, render_template

app = Flask(__name__)

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for the biography page
@app.route('/biography')
def biography():
    return render_template('biography.html')

# Route for the skills page
@app.route('/skills')
def skills():
    return render_template('skills.html')

# Route for the projects page
@app.route('/projects')
def projects():
    return render_template('projects.html')

# Route for the contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Route for the social media page
@app.route('/social')
def social():
    return render_template('social.html')

# Route for the additional info page
@app.route('/additional')
def additional():
    return render_template('additional.html')

if __name__ == '__main__':
    app.run(debug=True)
