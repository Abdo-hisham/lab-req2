from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    id = request.form['id']
    email = request.form['email']
    age = request.form['age']
    return render_template('result.html' , name = name , id = id , email = email, age = age )

if __name__ == '__main__':
    app.run()