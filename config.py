import configparser
import os, sys

path = os.path.dirname(os.path.realpath(__file__))

def analyze_conditions():
    
    #Essa função analisa se os arquivos da maid estão presentes
    #Se não estiver, esta função irá chamar outras funções para gerar estes arquivos
    
    if os.path.isdir(f'{path}/Configurações') == False:
        print("AVISO: Arquivos de configuração não foram encontrados!")
        print("Gerando arquivos...")
        os.mkdir(f'{path}/Configurações')
        mkconf_main()
        mkconf_voz()
        mkconf_tts()
        mkconf_custom()
        print("Arquivos de configuração gerados com sucesso!")
        print("Reinicie a maid para poder utiliza-lá.")
        input('(Pressione qualquer tecla para reiniciar a maid...)')
        os.execl(sys.executable, sys.executable, *sys.argv)
    else:
        if os.path.isfile(f'{path}/Configurações/Principal.ini') == False:
            mkconf_main()
        if os.path.isfile(f'{path}/Configurações/Reconhecimento_de_voz.ini') == False:
            mkconf_voz()
        if os.path.isfile(f'{path}/Configurações/TTS.ini') == False:
            mkconf_tts()
        if os.path.isfile(f'{path}/Configurações/Customizações.ini') == False:
            mkconf_custom()
    
    if os.path.isdir(f'{path}/UserData') == False:
        os.mkdir(f'{path}/Userdata')
                        
    if os.path.isfile(f'{path}/Configurações/session.info') == True:
        os.remove(f'{path}/Configurações/session.info')
        mkconf_session()
    else:
        mkconf_session()
    
##################################################################################################
#A seguir se encontram as funções responsaveis por
#Gerar as configurações
##################################################################################################

def mkconf_main():
    
    #Função usada para gerar a
    #Configuração principal
    
    config = configparser.ConfigParser(allow_no_value=True)
    config['Version'] = {
        '; NAO ALTERE ESTES VALORES.': None,
        '; ELES SAO UTILIZADOS PARA ATUALIZAR A MAID.': None,
        'version': '0.5',
        'type': 'normal-app-exe',
    }
    config['Geral'] = {
        '; Caso o valor esteja como "true", habilitara o terminal. Valor padrao: "true"': None,
        'mostrar-terminal': 'true',
        ' ': None,
        '; Caso o valor esteja como "false", desabilitara o TTS.':  None,
        '; Caso desabilite essa funcao juntamente com a funcao "mostrar-terminal", a maid nao funcionara.': None,
        '; Valor padrao: "true"': None,
        'tts': 'true',
        '    ': None,
        '; Caso o valor esteja como "false", desabilita o controle por voz da maid. Valor padrao: "true"': None,
        'voice': 'true',
        '  ': None,
        '; Caso o valor esteja como "true", iniciara a maid como administrador/root. Valor padrao: "false"': None,
        'admin': 'false',
        '   ': None,
        '; Caso o valor esteja como "true", a maid ficara completamente offline. Valor padrao: "false"': None,
        'modo-offline': 'false',
        '     ': None,
        '; Define a frase utilizada para ativar a maid. Valor padrao: "ok maid"': None,
        'prefixo': 'executar',
        '      ': None,
        '; Caso o valor esteja como "false", a checagem automatica de updates sera desativada. Valor padrao: "true"': None,
        'checar-updates': 'true',
        '       ': None,
        '; Caso o valor esteja como "true", e o valor de "checar-updates" tambem estiver em "true"': None,
        '; O update sera baixado automaticamente': None,
        'baixar-updates': 'false',
    }
    with open(f'{path}/Configurações/Principal.ini', 'w') as configfile1:
        config.write(configfile1)    

def mkconf_voz():
    
    #Função usada para gerar a
    #Configuração de voz

    config = configparser.ConfigParser(allow_no_value=True)
    
    config['STT'] = {
    '; Aviso: estas opcoes surtirao efeito apenas se o reconhecimento de voz estiver habilitado': None,
    '': None,
    '; Ajusta a sensibilidade do microfone, e define um timeout adequado.': None,
    '; Deixe o valor como "0" para desativar esta funcao.': None,
    '; Deixe como "auto" para detectar um valor ideal automaticamente.': None,
    '; Valor padrao: "auto"': None,
    'sensibilidade': 'auto',
    ' ': None,
#    '; Se a sensibilidade estiver como "auto" e esta configuração estiver como "true", recheca a sensibilidade': None,
#    '; Toda vez que a maid utilizar o reconhecimento de voz. Valor padrão: "false"': None,
#    'sempre-ajustar': "false",
#    '     ': None,
    '; Define a engine que sera utilizada para reconhecimento de voz. Caso a maid esteja em modo offline, sera utilizado sphinx': None,
    '; Engines validas: "sphinx", "google", "google-cloud", "bing", "ibm", "wit", "houndify"': None,
    '; Valor padrao: "google"': None,
    'engine': 'google',
    '  ': None,
    '; Define o microfone que sera utilizado para reconhecimento de voz. Mude este numero caso queira utilizar outro microfone': None,
    '; Valor padrao: "1"': None,
    'microfone': '1',
    '   ': None,
    '; Define a quantidade de tempo que a maid ira esperar para processar a frase dita.': None,
    '; Caso o valor seja "0", a maid nao ira funcionar.': None,
    '; Caso o valor "sensibilidade" esteja ativado, o timeout nao ira funcionar.': None,
    '; Valor padrao: "2"': None,
    'timeout': '2',
    '    ': None,
    '; Define em que linguagem a voz sera interpretada. Valor padrao: "pt-br"': None,
    'linguagem': 'pt-br'
    }
    with open(f'{path}/Configurações/Reconhecimento_de_voz.ini', 'w') as configfile2:
        config.write(configfile2)
        
def mkconf_tts():
    
    #Função usada para gerar a
    #Configuração de TTS

    config = configparser.ConfigParser(allow_no_value=True)
    
    config['TTS'] = {
    '; AVISO: ESTAS OPCOES APENAS SURTIRAO EFEITO SE O TTS ESTIVER HABILITADO': None,
    '': None,
    '; Define a engine que sera utilizada para fala. Valor padrao: "gtts"': None,
    '; Engines disponiveis: gtts, ttsx3, watson': None,
    'tts-engine': 'gtts',
    }
    config['TTSX3'] = {
    '; AVISO: ESTAS OPCOES APENAS SURTIRAO EFEITO SE A ENGINE DO TTS FOR "TTSX3"': None,
    '; Define a engine que sera utilizada no ttsx3. Valor padrao: "sapi5"': None,
    '; Engines disponiveis: espeak, sapi5, nsss': None,
    'engine': 'sapi5',
    '    ': None,
    '; Muda a voz sendo utilizada no pyttsx3.': None, 
    '; Caso queira usar uma outra voz instalada no sistema, mude este numero de 1 em 1.': None,
    '; Valor padrao: "1"': None,
    "id": '1',
    '       ': None,
    '; Insira o volume da voz desejado abaixo (Minimo = 0, Maximo = 1). Valor padrao: "0.5"': None,
    'volume': '0.5',
    }
    config['GTTS'] = {
    '; Define a linguagem utilizada. Valor padrao: "pt"': None,
    'linguagem': 'pt',
    '     ': None,
    '; Define o tld da api TTS da google (raramente precisa ser mudado). Valor padrao: "com.br"': None,
    'tld': 'com.br',
    }
    config['WATSON'] = {
    '; Define a voz que sera utilizada. Para uma lista de vozes disponiveis, acesse o link abaixo.': None,
    '; https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-voices': None,
    '; Valor padrao: pt-BR_IsabelaV3Voice': None,
    'watson-voice': 'pt-BR_IsabelaV3Voice',
    '        ': None,
    '; Define o formato em que o audio sera salvo. Valor padrao: "mp3"': None,
    '; Formatos disponiveis: mp3, wav, ogg': None,
    'watson-format': 'mp3'
    }
    with open(f'{path}/Configurações/TTS.ini', 'w') as configfile3:
        config.write(configfile3)

def mkconf_custom():
    
    #Função usada para gerar o arquivo
    #que irá conter a maioria das customizações da maid
    
    config = configparser.ConfigParser(allow_no_value=True)

    config["Custom"] = {
    ';Muda o nome da maid na maior parte das referencias a ela.': None,
    'name': 'maid',
    '': None,
    ';Muda o titulo da janela da maid.': None,
    'title': 'Maid',
    ' ': None
    }

    with open(f'{path}/Configurações/session.info', 'w') as file: 
        config.write(file)
    

def mkconf_session(): 

    #Função usada para gerar o arquivo
    #que irá conter as informações da sessão
    
    config = configparser.ConfigParser(allow_no_value=True)

    config["Session"] = {
    "online": '', 
    "tts": '',
    'google': '',
    "mic-output": '',
    'tempnote': 'a',
    }

    with open(f'{path}/Configurações/session.info', 'w') as file: 
        config.write(file)