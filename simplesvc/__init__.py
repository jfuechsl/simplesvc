from flask import Flask, render_template

from .volumes import get_mounts
from .envvars import get_environment_variables
from .xkcd import get_current_xkcd

app = Flask(__name__)

@app.route('/')
def root_route():
  mounts = get_mounts()
  env_vars = get_environment_variables('EY_')
  xkcd = get_current_xkcd()
  return render_template('svcinfo.html', mounts=mounts, env_vars=env_vars, xkcd=xkcd)
