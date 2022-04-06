
def reloadNukeArcane2():
    ''' reload arcane2 modules '''
    print('Reloading Arcane2 modules')
    import sys
    for k in sys.modules.keys():
        if k.lower().startswith('a2') or k.lower().startswith('nuke_tools_py3'):
            print(f'Deleting: {k.lower()}')
            del sys.modules[k]
    print('/_' * 50)
    print('Done')
