from psnawp_api import PSNAWP
import requests
def get_trophies_by_group(ssoKey, title_id, group_id, language="pt-br"):
  psnawp = PSNAWP(ssoKey)
  client = psnawp.me()
  trophies = client.trophy_titles_for_title([title_id])
  all_trophies = []
  for trophy in trophies:
    # defined_trophies = client.trophies(trophy.np_communication_id, platform=trophy.title_platform, trophy_group_id=group_id, include_metadata=True)
    # for defined_trophy in defined_trophies:
    #   all_trophies.append({"name": defined_trophy.trophy_name, "icon": defined_trophy.trophy_icon_url, "type": defined_trophy.trophy_type.name, "description": defined_trophy.trophy_detail, "earned": defined_trophy.earned})
    auth_token = client._request_builder.authenticator._auth_properties["access_token"]
    earned_trophies = requests.get("https://m.np.playstation.com/api/trophy/v1/users/me/npCommunicationIds/%s/trophyGroups/%s/trophies"%(trophy.np_communication_id, group_id), params={'npServiceName': 'trophy'}, headers={'Authorization': 'Bearer %s'%(auth_token), 'Accept-Language': language})
    earned_json = earned_trophies.json()
    result = requests.get("https://m.np.playstation.com/api/trophy/v1/npCommunicationIds/%s/trophyGroups/%s/trophies"%(trophy.np_communication_id, group_id), params={'npServiceName': 'trophy'}, headers={'Authorization': 'Bearer %s'%(auth_token), 'Accept-Language': language})
    json_result = result.json()
    for defined_trophy in json_result['trophies']:
      all_trophies.append({"name": defined_trophy['trophyName'], "icon": defined_trophy['trophyIconUrl'], "type": defined_trophy['trophyType'], "description": defined_trophy['trophyDetail'], "earned": len(list(filter(lambda troph: troph['trophyId'] == defined_trophy['trophyId'] and troph['earned'],earned_json['trophies']))) > 0})
  return all_trophies