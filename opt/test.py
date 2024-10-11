from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="utf-8">
      <title>Hello Page</title>
    </head>
    <body>
      <h1>Hello, World!</h1>
      <p>This is a simple page served by Flask.</p>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)


