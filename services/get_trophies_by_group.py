from psnawp_api import PSNAWP
def get_trophies_by_group(ssoKey, title_id, group_id):
  psnawp = PSNAWP(ssoKey)
  client = psnawp.me()
  trophies = client.trophy_titles_for_title([title_id])
  all_trophies = []
  for trophy in trophies:
    defined_trophies = client.trophies(trophy.np_communication_id, platform=trophy.title_platform, trophy_group_id=group_id, include_metadata=True)
    for defined_trophy in defined_trophies:
      all_trophies.append({"name": defined_trophy.trophy_name, "icon": defined_trophy.trophy_icon_url, "type": defined_trophy.trophy_type.name, "description": defined_trophy.trophy_detail})
  return all_trophies