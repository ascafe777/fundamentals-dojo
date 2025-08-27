#!/usr/bin/env python3
from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def root():
    return "Server is listening on port 1337"

if __name__ == "__main__":
    app.run(host="localhost", port=1337)
