from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():

    url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSz5oLvAwhcA7d8Uryc4JSOW6SnGP0-8mrv7PB05Kyg5uJJSr6p_b_A2yXhentLeYt_nx9rcFV1tyRE/pub?output=csv"
    df = pd.read_csv(url)

    # Get cell A1
    value = df.iloc[0,0]

    return render_template("main.html", cell_value=value)

if __name__ == "__main__":
    app.run(debug=True)