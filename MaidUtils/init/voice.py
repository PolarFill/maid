import configparser
from config import path
config = configparser.ConfigParser()

config.read([f'{path}/Configurações/Reconhecimento_de_voz.ini', f'{path}/Configurações/session.info'])
microfone = config.getint('STT', 'microfone')
sensibilidade = config.get('STT', 'sensibilidade')           
engine2 = config.get('STT', 'engine').lower()
timeout = config.getint('STT', 'timeout')
lang = config.get('STT', 'linguagem')

if sensibilidade != 'auto':
    float(sensibilidade)

def capture():    #Função responsavel por capturar input
    import speech_recognition as sr
    from colorama import Fore, init
    r = sr.Recognizer()
    init()

    print(Fore.RED + "\033[KPegando dispositivo...", end='\r')
    if microfone == 1:                                #Pegando microfone definido pelo usuarío nas configs
        mic = sr.Microphone()                         #Caso o mic n seja 1 (principal), vai usar o definido pelo usuario
    else:
        mic = sr.Microphone(device_index=microfone)  

    print(Fore.YELLOW + "\033[KAjustando sensibilidade...", end='\r')
    with mic as source:
        if sensibilidade != '0':                      #Detectando a sensibilidade do mic
            if sensibilidade == 'auto':               
                r.adjust_for_ambient_noise(source)    #Caso esteja como auto, a sensibilididade sera ajustada
            else:
                r.adjust_for_ambient_noise(source, duration=sensibilidade)
        
        print(Fore.GREEN + "\033[KCaptando audio!", end='\r')
        if timeout != 0 and timeout > 0:              #Checando se o usuario definiou um timeout
            audio = r.listen(source, phrase_time_limit=timeout)
        else:
            audio = r.listen(source)

    if audio == None:
        print(Fore.RED + "Nada foi dito." + Fore.RESET)
    else:
        print(Fore.CYAN + "\033[KReconhecendo audio...")

    try:
        if engine2 == 'google':     #Engines e keys da api da google (não confundir com google cloud)
            output = r.recognize_google(audio, key='AIzaSyAOC9oUf5AjOweXeEOowokEye6VRPx8cZo', language=lang)
        elif engine2 == 'wit':      #Engines e keys da api da wit
            if 'en' in lang:
                output = r.recognize_wit(audio, key='IUIX2CGM5KIJDU43PR5B3SL5PGZQHZCL')    #key de reconhecimento em ingles
            else:
                output = r.recognize_wit(audio, key='AAAK2MMLZVTDXRRCCZLMLLSPVFREAVRE')    #key em pt (padrão)
        else:
            output = r.recognize_wit(audio, key='AAAK2MMLZVTDXRRCCZLMLLSPVFREAVRE')        #por padrão, usa key da wit
        output.lower()                                                                     #coloca o output em minusculo

        print(Fore.BLUE + "Input:" + Fore.CYAN + f" {output}" + Fore.RESET)
        return output
    except ValueError: #essa exceção é levantada caso o usuarío não diga nada
        print(Fore.RED + "Nada foi dito." + Fore.RESET)
        pass
    except sr.UnknownValueError: #não lembro quando essa exceção é levantada (top 10 programadores)
        print(Fore.RED + "Nada foi dito." + Fore.RESET)
        pass