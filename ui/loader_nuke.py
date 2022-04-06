
from PySide2 import QtWidgets


class LoaderNuke():
    ''' provides classmethods for load qtDesigner ui files into python scripts '''

    @staticmethod
    def getNukeWindow():
        '''Get the Nuke main window'''
        return QtWidgets.QApplication.activeWindow()

    @staticmethod
    def getNukeMainWindow():
        ''' Returns Nuke's main window '''
        for obj in QtWidgets.qApp.topLevelWidgets():
            if (obj.inherits('QMainWindow') and
                    obj.metaObject().className() == 'Foundry::UI::DockMainWindow'):
                return obj

        raise RuntimeError('Could not find DockMainWindow instance')
