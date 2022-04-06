Arcane2 Nuke Tools Python3
==========================

Maximiliano Rocamora / maxirocamora@gmail.com

Tested on:
Nuke 13

Install
=======

on *init.py*
nuke.pluginAddPath(f'{NUKE_TOOLS_ROOT}/arcane/{ENV}/plugin')

*menu.py*
loads arcane2 menu bar into nuke

*init.py*
loads Arcane2 Nuke path into nuke plugins path

Tools
=====

Comp Manager
------------
Handles nuke script files
Features
+ Open last comp from given shot area (lightComp, Comp, HelpScript)
+ Creates a new comp with naming convention and version.
+ Creates new folder for helpscripts
+ Can browse and save current comp/shot
+ Save last Project/Sequences selected and restores on reopening.
+ Show on preview windows last published of this comp

Shot Browser
------------
A helper function to open pipeline related folder paths

Writecane
---------
Script Write Tool for Arcane Projects.  
Generates Write nodes for local/deadline output.  

Reload Arcane2
--------------
A development helper function to reload Arcane2 modules from nuke
