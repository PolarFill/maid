def runSave():
    import pyscreeze, datetime, os
    import platform
    from config import path

    if os.path.isdir(f'{path}/UserData/Screenshots') == False:
        os.mkdir(f'{path}/UserData/Screenshots')

    if platform.system().startswith('W'):
        pyscreeze.screenshot('{}\\UserData\\Screenshots\\Screenshot-{}.png'.format(path, datetime.datetime.now()))
    else:
        pyscreeze.screenshot('{}/UserData/Screenshots/Screenshot-{}.png'.format(path, datetime.datetime.now()))