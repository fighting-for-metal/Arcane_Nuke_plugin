''' LOADS ARCANE MENU ON NUKE FROM INI FILE
[MENUBAR]
Main menu item
[type]
script (added to the menus with command and shortcut )
subMenu (added as a submenu)
[tree]
root (added to the root arcane menu)
subMenu (added to the last submenu created)
'''
import os
import configparser

import nuke

menuConfigFile = os.path.join(os.path.dirname(__file__), 'nuke_menu.ini')


class ArcaneMenuCreator():
    def __init__(self):
        ''' creates nuke menu based on config file '''
        self.parser = configparser.ConfigParser()
        self.parser.read(menuConfigFile)
        self.rootMenuLabel = self.parser.get('MENUBAR', 'label')
        if nuke.GUI:
            self.createHeader(self.rootMenuLabel)
            self.parseMenu()

    def createHeader(self, label):
        ''' creates main menu '''
        self.menubar = nuke.menu('Nuke')
        self.rootArcaneMenu = self.menubar.addMenu(label)

    def parseMenu(self):
        ''' parses ini file and creates menuitems '''
        for option in self.parser.sections():
            menuType = self.parser.get(option, 'type')
            label = self.parser.get(option, 'label')
            command = self.parser.get(option, 'command')
            tree = self.parser.get(option, 'tree')
            shortcut = self.parser.get(option, 'shortcut')
            if menuType == 'subMenu':
                self.lastMenu = self.createSubMenuGroup(label)
            elif menuType == 'script':
                if tree == 'root':
                    self.addCommandItem(self.rootArcaneMenu,
                                        label, command, shortcut)
                else:
                    self.addCommandItem(
                        self.lastMenu, label, command, shortcut)

    def createSubMenuGroup(self, label):
        ''' creates a submenu '''
        return self.rootArcaneMenu.addMenu(label)

    def addCommandItem(self, menuItem, label, command, shortcut):
        ''' creates item menu '''
        menuItem.addCommand(label, command, shortcut)
