# -*- coding: utf-8 -*-
import os

import nuke

from a2api.api_entity import ArcaneEntityAPI


def pipeline_names():
    ''' returns sequence and shot name from opened file '''
    try:
        path = nuke.Root()['name'].value()
        folder = os.path.split(path)[0]
        seq_name = folder.split('/')[3]
        shot_name = folder.split('/')[4]
    except ValueError:
        return False

    return seq_name, shot_name


def version():
    ''' Returns "v####" version from opened file
    Takes last numbers of file to get version
    Always return 'v####' format
    '''
    path = nuke.Root()['name'].value()
    filename = os.path.split(path)[1]
    for counter, index in enumerate(reversed(filename)):
        if not index.isdigit():
            limit = counter
            break
    return 'v' + filename[-limit:].zfill(4)


def get_shot_document(pid: int):
    ''' returns arcane2 current shot from opened nukescript
    Args:
        api (class) arcane2 api class
        pid (int) project id
    '''
    api = ArcaneEntityAPI()

    # get sequence and shot index from names
    seq_name, shot_name = pipeline_names()
    if not seq_name:
        return

    seq = api.find('sequence', {'pid': pid, 'name': seq_name})
    if not seq.ok:
        nuke.tprint('Failed Sequence Query.')
        return

    shot = api.find('shot', {'pid': pid,
                             'name': shot_name,
                             'parent_id': seq['index']}
                    )
    if not shot.ok:
        nuke.tprint('Failed Shot Query.')
        return

    return shot
