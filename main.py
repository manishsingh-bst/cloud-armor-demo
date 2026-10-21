import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    service_name = os.environ.get("K_SERVICE", "unknown")
    return f"hello, this site is serving on {service_name} cloudrun"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
