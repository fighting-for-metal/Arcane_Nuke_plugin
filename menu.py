'''
menu.py nuke13
create Max Rocamora / maxirocamora@gmail.com
editor Milton Maguna / milton.maguna@gmail.com
3.0.1 - 02/2022 - Python3 revision
3.1.0 - 06/04/2020 - new structure of pipeline @ Milton Maguna
'''
import os 
import sys

import nuke

# ---------------------------------------------------------------------------------------
# add external libraries [jsonmd, requests, kids-cache, cachetools]
# ---------------------------------------------------------------------------------------

sys.path.append("C:/Python/Python39/Lib/site-packages")

from a2core.arbiter import Arbiter
from a2studio.setenv.env_setup import EnvironmentSetup
from jsonmd.json_utils import load_json, save_json

# -----------------------------------------------------------------------------
# set project ARCANE2
# -----------------------------------------------------------------------------

def set_project_load_scripts():
    home = os.path.expanduser('~')
    path_json = os.path.join(home, "Arcane2", "set_project.json")

    if os.path.exists(path_json):
        data = load_json(path_json)

        pid = data['last_project_pid']
        es = EnvironmentSetup()
        es.activate_project(pid)
        nuke.tprint('Loading Project ', pid)
    else: 
        nuke.tprint('no Set project')

nuke.addOnScriptLoad(set_project_load_scripts, nodeClass='Root')

# ---------------------------------------------------------------------------------------
# MENU & TOOLBAR
# ---------------------------------------------------------------------------------------

print('/-' * 30)
print(f'LOADING ARCANE2 MENU - {nuke.NUKE_VERSION_STRING}')
print('/-' * 30)

from ui.arcaneMenu import ArcaneMenuCreator
ArcaneMenuCreator()

# -----------------------------------------------------------------------------
# DEFAULTS NODES
# -----------------------------------------------------------------------------

import custom_gizmo.studio_defaults_nodes
import custom_gizmo.studio_callbacks

# -----------------------------------------------------------------------------
# SHORCUTS
# -----------------------------------------------------------------------------

import custom_gizmo.studio_shorcut

# -----------------------------------------------------------------------------
# OPEN TOOLS
# -----------------------------------------------------------------------------

import custom_gizmo.open_tools
