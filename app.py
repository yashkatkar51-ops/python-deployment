from flask import Flask, render_template, jsonify

app = Flask(__name__, static_folder="static", template_folder="templates")


@app.route("/")
def home():
    return render_template("index.html", title="My Static Python App for deployment")


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/health")
def health():
    # Handy for load balancers / uptime checks
    return jsonify(status="ok"), 200


if __name__ == "__main__":
    # Local development only. In production Gunicorn runs the app.
    app.run(host="0.0.0.0", port=5000, debug=True)
