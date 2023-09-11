from psnawp_api import PSNAWP
import requests
def get_trophy_groups(ssoKey, title_id, language='pt-br'):
  psnawp = PSNAWP(ssoKey)
  client = psnawp.me()
  trophies = client.trophy_titles_for_title([title_id])
  result = {}
  for trophy in trophies:
    print(trophy.np_communication_id)
    trophy_info = client.trophy_groups_summary(trophy.np_communication_id, trophy.title_platform, True)
    trophy_groups = []
    auth_token = client._request_builder.authenticator._auth_properties["access_token"]
    result = requests.get("https://m.np.playstation.com/api/trophy/v1/npCommunicationIds/%s/trophyGroups"%(trophy.np_communication_id), params={'npServiceName': 'trophy'}, headers={'Authorization': 'Bearer %s'%(auth_token), 'Accept-Language': language})
    result_json = result.json()
    for group in result_json['trophyGroups']:
      trophy_groups.append({"name": group['trophyGroupName'], "icon": group['trophyGroupIconUrl'], "group_id": group['trophyGroupId'] })
    # for group in trophy_info.trophy_groups:
    #   # all_trophies = []
    #   # defined_trophies = client.trophies(trophy.np_communication_id, platform=trophy.title_platform, trophy_group_id=group.trophy_group_id, include_metadata=True)
    #   # for defined_trophy in defined_trophies:
    #   #   all_trophies.append({"name": defined_trophy.trophy_name, "icon": defined_trophy.trophy_icon_url, "type": defined_trophy.trophy_type.name})
    #   trophy_groups.append({"name": group.trophy_group_name, "icon": group.trophy_group_icon_url, "group_id": group.trophy_group_id })
    result = {
      "name": trophy.title_name,
      "image": trophy.title_icon_url,
      "total_trophies": (trophy_info.defined_trophies.bronze + trophy_info.defined_trophies.silver + trophy_info.defined_trophies.gold + trophy_info.defined_trophies.platinum), 
      "earned_trophies":(trophy_info.earned_trophies.bronze + trophy_info.earned_trophies.silver + trophy_info.earned_trophies.gold + trophy_info.earned_trophies.platinum),
      "progress": trophy.progress,
      "groups": trophy_groups
      }
  return result