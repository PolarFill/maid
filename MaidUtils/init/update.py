def Check(): #Checa por updates no repositório
    import configparser
    from config import path
    
    config = configparser.ConfigParser()
    config.read(f"{path}/Configurações/Principal.ini")
    
    if config.get('Geral', 'checar-updates').lower() == 'true':
        import requests

        print("Checando updates...")

        #COMPLETAR DEPOIS

        #Fazer o requests pegar a tag da versão atual no github.
        #Avisar q tem updates, e, se o usuario quiser, baixar
        #A versão ideal para ele. (da pra fazer tudo com requests se souber)

        #request = requests.get()