"""Flask-приложение о здоровом питании."""
from flask import Flask, render_template

from data_products import PRODUCTS

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/o-pitanii")
def about_nutrition():
    return render_template("nutrition.html")


@app.route("/kalkulyator")
def calculator():
    return render_template("calculator.html")


@app.route("/produkty")
def products():
    return render_template("products.html", products=PRODUCTS)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
