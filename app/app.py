from flask import Flask, render_template

app = Flask(__name__)

stocks = [
    {"name": "RELIANCE", "price": 1425.50, "change": 3.42},
    {"name": "TCS", "price": 3812.20, "change": 2.81},
    {"name": "INFY", "price": 1722.40, "change": 2.35},
    {"name": "HDFCBANK", "price": 1612.10, "change": -2.14},
    {"name": "WIPRO", "price": 412.30, "change": -2.91},
    {"name": "ADANI", "price": 1018.20, "change": -3.82},
]


@app.route("/")
def dashboard():
    top_performers = sorted(
        stocks,
        key=lambda x: x["change"],
        reverse=True
    )[:3]

    worst_performers = sorted(
        stocks,
        key=lambda x: x["change"]
    )[:3]

    return render_template(
        "index.html",
        top_performers=top_performers,
        worst_performers=worst_performers
    )


@app.route("/health")
def health():
    return {"status": "healthy"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)