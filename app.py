from flask import Flask, jsonify, request
from services.get_games_stats import get_games_stats
from services.get_own_info import get_own_info
app = Flask(__name__)
@app.route('/get_stats', methods=['GET'])
def get_stats():
  token = request.args.get("token")
  return jsonify(get_games_stats(token))

@app.route('/get_own_info', methods=['GET'])
def get_info():
  token = request.args.get("token")
  return jsonify(get_own_info(token))

app.run(host='0.0.0.0' )