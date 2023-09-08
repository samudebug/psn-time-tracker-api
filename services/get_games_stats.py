from psnawp_api import PSNAWP
def get_games_stats(ssoKey):
  psnawp = PSNAWP(ssoKey)
  client = psnawp.me()
  stats = client.title_stats()
  data = []
  
  for x in stats:
    h = int(x.play_duration.total_seconds()//3600)
    m = int((x.play_duration.total_seconds()%3600)//60)
    data.append({"title_id": x.title_id,"name": x.name, "total_play_duration": "%s horas %s minutos"%(h,m), "image_url": x.image_url})
  return data

