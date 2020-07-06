from flask import Flask
from flask import render_template
app = Flask(__name__)


# if you hit root or home you will still see this functionality
@app.route('/')
@app.route('/home')
def hello_world():
    return render_template('homepage.html', title='Homepage')


@app.route('/about')
def about():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>about</title>
    </head>
    <body>
        <div>
        <h1>This is about</h1>
        </div>
    </body>
    </html>
    '''


if __name__ == '__main__':
    app.run()
