import requests

def _unsuccessful_result():
  return {
    'success': False
  }

def _successful_result(result):
  return {
      'success': True,
      'data': result
    }

def get_current_xkcd():
  try:
    r = requests.get('https://xkcd.com/info.0.json', timeout=5)
    if r.status_code != requests.codes.ok:
      return _unsuccessful_result()
    else:
      return _successful_result(r.json())
  except:
    return _unsuccessful_result()
