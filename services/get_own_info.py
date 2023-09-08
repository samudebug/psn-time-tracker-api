from psnawp_api import PSNAWP

def get_own_info(ssoKey):
  psnawp = PSNAWP(ssoKey)
  client = psnawp.me()
  user = client.get_profile_legacy()
  return {"name": user["profile"]["onlineId"], "avatarUrl": user["profile"]["avatarUrls"][0]["avatarUrl"]}