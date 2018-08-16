import requests

def get_current_xkcd():
  r = requests.get('https://xkcd.com/info.0.json')
  if r.status_code != requests.codes.ok:
    return {
      'success': False
    }
  else:
    return {
      'success': True,
      'data': r.json()
    }
