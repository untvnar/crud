from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>My First Python Page</title>
    </head>
    <body>
        <h1>Hello!</h1>
        <p>My name is Francis.</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run()
