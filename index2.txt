from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def home():
    url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRjkdsPv1vbXtvixd2FBYJzbR3QDUYGgfIykgLN0_-xZBPDl3nN898KaMmZY_FCBFXOkFXKSaytcQYM/pub?output=csv"

    csv_data = requests.get(url).text

    rows = csv_data.strip().splitlines()
    b6 = rows[5].split(",")[1]

    return f"""
    <html>
        <body>
            <h1>Cell B6</h1>
            <h2>{b6}</h2>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)