from psnawp_api import PSNAWP
def get_trophy_groups(ssoKey, title_id):
  psnawp = PSNAWP(ssoKey)
  client = psnawp.me()
  trophies = client.trophy_titles_for_title([title_id])
  result = {}
  for trophy in trophies:
    trophy_info = client.trophy_groups_summary(trophy.np_communication_id, trophy.title_platform, True)
    trophy_groups = []
    for group in trophy_info.trophy_groups:
      # all_trophies = []
      # defined_trophies = client.trophies(trophy.np_communication_id, platform=trophy.title_platform, trophy_group_id=group.trophy_group_id, include_metadata=True)
      # for defined_trophy in defined_trophies:
      #   all_trophies.append({"name": defined_trophy.trophy_name, "icon": defined_trophy.trophy_icon_url, "type": defined_trophy.trophy_type.name})
      trophy_groups.append({"name": group.trophy_group_name, "icon": group.trophy_group_icon_url, "group_id": group.trophy_group_id })
    result = {
      "name": trophy.title_name,
      "image": trophy.title_icon_url,
      "total_trophies": (trophy_info.defined_trophies.bronze + trophy_info.defined_trophies.silver + trophy_info.defined_trophies.gold + trophy_info.defined_trophies.platinum), 
      "earned_trophies":(trophy_info.earned_trophies.bronze + trophy_info.earned_trophies.silver + trophy_info.earned_trophies.gold + trophy_info.earned_trophies.platinum),
      "progress": trophy.progress,
      "groups": trophy_groups
      }
  return result