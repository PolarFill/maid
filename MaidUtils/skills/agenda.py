def TempNote(note): #Cria nota temporaria
    import configparser
    from config import path
    
    config = configparser.ConfigParser()
    config.read(f'{path}/Configurações/session.info')
    
    config.set('Session', 'tempnote', note) #Escreve nota temporaria
    with open(f'{path}/Configurações/session.info', 'w') as configfile: #Escreve o novo session.info
        config.write(configfile)
    
def ReadTempNote(): #Lê nota temporaria
    import configparser
    from config import path
    
    config = configparser.ConfigParser()
    config.read(f'{path}/Configurações/session.info')
    note = config.get('Session', 'tempnote')
    
    if note == '':
        note = 'Nenhuma nota foi encontrada.'
    
    return note