def get_mounts():
  try:
    with open('/proc/mounts', 'r') as f:
      mounts = [line.split()[1] for line in f.readlines()]
    return mounts
  except:
    return []
