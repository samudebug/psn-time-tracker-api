from flask import Flask, jsonify, request
from services.get_games_stats import get_games_stats
from services.get_own_info import get_own_info
from services.get_trophy_groups import get_trophy_groups
from services.get_trophies_by_group import get_trophies_by_group
app = Flask(__name__)
@app.route('/get_stats', methods=['GET'])
def get_stats():
  token = request.args.get("token")
  return jsonify(get_games_stats(token))

@app.route('/get_own_info', methods=['GET'])
def get_info():
  token = request.args.get("token")
  return jsonify(get_own_info(token))

@app.route('/get_trophy_groups/<title_id>')
def get_groups(title_id):
  token = request.args.get("token")
  
  # title_id = request.view_args['title_id']
  return jsonify(get_trophy_groups(token, title_id))

@app.route('/get_trophies/<title_id>/<group_id>')
def get_trophies(title_id, group_id):
  token = request.args.get("token")
  language = request.args.get("language")
  return jsonify(get_trophies_by_group(token, title_id, group_id, language=language))
app.run(host="0.0.0.0")
