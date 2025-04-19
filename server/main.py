from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
# may need to chagne to accept specific origins later
# currently set to accept all
cors = CORS(app, origins='*')

@app.route("/api/nba/stats", methods=(['GET']))
def nba_stats():
    return jsonify(
        message="NBA stats initial setup"
    )

if __name__ == "__main__":
    app.run(debug=True, port=8080)