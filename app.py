from flask import Flask
from flask import render_template
app = Flask(__name__)

dummyData = [
    {
        "fName": "David",
        "lName": "McCartney",
        "title": "Mr",
        "content": "some bhoy"
    },
    {
        "fName": "Tadas",
        "lName": "Vaidotas",
        "title": "Mr",
        "content": "lecturer boy"
    }
]

# if you hit root or home you will still see this functionality
@app.route('/')
@app.route('/home')
def home():
    return render_template('homepage.html', title='Homepage', posts=dummyData)


@app.route('/about')
def about():
    return render_template('aboutpage.html', title='Aboutpage')


if __name__ == '__main__':
    app.run()
