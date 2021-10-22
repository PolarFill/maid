def Youtube(search): #Pega musicas e etc do youtube
    import requests #Importa requests
    import platform #Importa o platform para analizar a plataforma
    import contextlib #Importa o pygame sem a mensagemKKKKKK
    import configparser #Seta no session.info que uma musica está tocando
    import youtube_dl #Importa ytdl pra pegar o mp3
    from config import path #Importa o path do config.py
    from youtubesearchpython import VideosSearch #Importa livraria para pesquisar no youtube
    with contextlib.redirect_stdout(None): #Importa o pygame com o stdout redirecionado para None
        import pygame                      #Para ele não mostrar a mensagem de import no terminal
    
    if platform.system().startswith('W'):                 #Caso o sistema seja windows
        audiopath = f"{path}\\Configurações\\tempytb.mp3" #O diretório do audio será composto de \
    else:                                                 #Caso não seja windows
        audiopath = f"{path}/Configurações/tempytb.mp3"   #O diretório do audio será composto de /
    
    args = {'format': 'mp3',                   #Define que o audio em melhor qualidade sera pego
            'noplaylist': 'True',              #Define que playlists não serão baixadas
            'outtmpl': f'{path}'}  #Define o nome do arquivo da musica
    
    pesquisa = VideosSearch(search, limit=1)
    resultado = pesquisa.result()
    
    config = configparser.ConfigParser()
    config.read(f'{path}/Configurações/session.info')
    
    with youtube_dl.YoutubeDL(args) as ydl:
        ydl.download(resultado['result']['link'])
        
    pygame.init()                                                #Iniciando pygame 
    pygame.mixer.init()                                          #Iniciando mixer
    pygame.mixer.music.load(audiopath)                           #Carregando musica
    pygame.mixer.music.play()                                    #Tocando audio
    while pygame.mixer.music.get_busy():                         #Espera o audio tocar para destruir o objeto
        pygame.time.Clock().tick(10)                             #Esperando...
    pygame.mixer.music.unload()                                  #Descarregando arquivo
    pygame.mixer.music.stop()                                    #Encerrando mixer                              
    os.remove(audiopath)                                         #Remove audio
        
    
    
#############################
#########FUNÇÃO DE CHECAGEM
#############################

def Check(): #Checa se alguma musica está tocando
    import configparser
    from config import path
    
    config = configparser.ConfigParser()
    config.read(f'{path}/Configurações/session.info') #Lendo arquivo de sessão
    
    if config.get('Session', 'spotify') == 'True': #Checando se spotify está tocando
        
        config.set('Session', 'spotify', 'False') #Se tiver, muda o valor de tocando pra inativo
        with open(f'{path}/Configurações/session.info', 'w') as configfile:
            config.write(configfile)
            
        return 'spotify' #Retorna que o spotify está ativo para assim matar o processo dele
    
    elif config.get('Session', 'youtube') == 'True': #checa se o youtube está tocando
        
        config.set('Session', 'youtube', 'False') #Se tiver, muda o valor de tocando pra inativo
        with open(f'{path}/Configurações/session.info', 'w') as configfile:
            config.write(configfile)
            
        return 'youtube' #Retorna que o youtube está ativo para assim matar o processo dele
    
    else:
        return 0