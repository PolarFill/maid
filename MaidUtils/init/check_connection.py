def Connection(): #Função responsavel por checar a conexão a internet do usuario
    import configparser
    from config import path
    config = configparser.ConfigParser()
    
    config.read([f'{path}/Configurações/session.info', 
                 f'{path}/Configurações/Principal.ini'])
    
    if config.get('Geral', 'modo-offline').lower() == "true":
        print("Maid iniciada automaticamente no modo offline. Caso deseje desabilitar isto, acesse as configurações principais.")
        config.set('Session', 'online', 'false')
        
        with open(f'{path}/Configurações/session.info', 'w') as configfile:
            config.write(configfile)

    else:
        try:
            import httplib
        except:
            import http.client as httplib
            
        ping = httplib.HTTPConnection("www.google.com", timeout=5)
        
        try:
            ping.request("HEAD", "/")
            ping.close()
            
            print("Maid conectada a internet com sucesso!")
            config.set('Session', 'online', 'true')
            with open(f'{path}/Configurações/session.info', 'w') as configfile:
                config.write(configfile)

        except:
            ping.close()
            print("Não foi possível realizar uma conexão com a internet.")
            config.set('Session', 'online', 'false')
            with open(f'{path}/Configurações/session.info', 'w') as configfile:
                config.write(configfile)
