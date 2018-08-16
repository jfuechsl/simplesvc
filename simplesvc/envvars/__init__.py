import os

def get_environment_variables(starting_with):
  return [[env_name, env_value] for env_name, env_value in os.environ.items() if env_name.startswith(starting_with)]
