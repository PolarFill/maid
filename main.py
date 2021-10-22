###################################
###Esta é a parte onde o input da maid é pego e reconhecido
###################################

answers_cancelar = ['cancelar', 'nada', 'esquece', 'deixa']
answers_dado = ['jogue um dado', 'joga um dado', 'jovem um dado', 'role um dado', 'dado']
answers_say = ['diga', 'fale', 'funny', 'Funny', 'repita']
answers_print = ['print', 'screenshot', 'tire uma foto da tela']
answers_sair = ['sair', 'fechar', 'saiu', 'fechou', 'desligar']
answers_ReadTempNote = ['leia uma nota temporaria', 'leia a nota temporaria', 'diga a nota temporária', 'Diga a nota temporária']
answers_tempnote = ['nota temporaria', 'crie uma nota temporaria', 'faça uma nota temporaria', 'mota temporaria', 'nota temporária']
answers_speednet = ['speedtest', 'velocidade da internet', 'teste de velocidade', 'velocidade da net', 'speed test']
answers_window = ['pegar janela', 'janela', 'window']
answers_volume = ['']

def eternal_input():
    from MaidUtils.init.tts import say          #Importando função do tts
    from MaidUtils.init.voice import capture    #Importando função de captura de fala

    import configparser
    from config import path
    config = configparser.ConfigParser()
    config.read([f'{path}/Configurações/session.info', f'{path}/Configurações/Principal.ini'])   #Lendo configs

    prefixo = config.get("Geral", 'prefixo').lower()

    while True:
        cmd = capture()
        
        try:
            if cmd == prefixo:
                say("Olá! No que posso te ajudar?")
                cmd = capture()

                if cmd in answers_print: #Copia print da tela no clipboard
                    import MaidUtils.skills.screenshot
                    MaidUtils.skills.screenshot.runSave()
                    say('Screenshot salva na pasta "Screenshots".')

                elif cmd in answers_dado: #Rola um dado
                    import MaidUtils.skills.dice
                    resultado = MaidUtils.skills.dice.roll()
                    say(f"O resultado é: {resultado}")

                elif "dado de " in cmd: #Rola um número definido pelo usuario
                    import MaidUtils.skills.dice, re
                    re.sub('\D', '', cmd) #Substituindo todas as letras por whitespace
                    MaidSkills.dice.roll_custom(cmd)
                    say(f"O resultado é: {resultado}")
                    
                elif cmd in answers_tempnote: #Escreve uma nota temporaria
                    import MaidUtils.skills.agenda
                    say("O que deseja anotar?")
                    note = capture()
                    MaidUtils.skills.agenda.TempNote(note)
                    say("Nota temporária escrita!")
                    
                elif cmd in answers_ReadTempNote: #Lê a nota temporaria
                    import MaidUtils.skills.agenda
                    note_returned = MaidUtils.skills.agenda.ReadTempNote()
                    say(note_returned)
                    
                elif cmd in answers_speednet:
                    import MaidUtils.skills.speedtest_net
                    say("Aguarde...")
                    MaidUtils.skills.speedtest_net.Test()

                elif cmd in answers_sair: #Fecha a maid
                    say("Saindo...")
                    sys.exit("Fechando maid...")
                    
                elif cmd in answers_window:
                    import MaidUtils.skills.get_window
                    MaidUtils.skills.get_window.Manipulate()
                    
                elif cmd in answers_say: #Faz a maid falar algo
                    say("O que deseja que eu fale?")
                    fala = capture()
                    if fala != None:
                        say(fala)
                    else:
                        say("Desculpe, não entendi o que quis dizer.")

                elif cmd in answers_cancelar: #Cancela input
                    pass
                
                ##############################################TOCAR MUSICAS E ETC
                
                elif cmd.startswith('youtube ') or cmd.startswith('YouTube '): #Toca musicas do youtube
                    import multiprocessing
                    import MaidUtils.skills.play_songs
                    cmd.replace('YouTube ', '')
                    YoutubePlay = multiprocessing.Process(target=MaidUtils.skills.play_songs.Youtube, args=(cmd,))
                    YoutubePlay.start()
                    
                
                elif cmd == 'parar musica':
                    import MaidUtils.skills.play_songs
                    check = MaidUtils.skills.play_songs.Check()
                    if check == 'youtube':
                        YoutubePlay.kill()
                        print("b")
                    elif check == 'spotify':
                        SpotifyPlay.kill()
                    else:
                        say("Nenhuma musíca está tocando no momento")
                
                ###############################################else e exceções    

                else: #Fala que o input não foi reconhecido
                    say('Desculpe, não entendi.')
                    
        except TypeError: #Caso o usuario não fale nada se n me engano
            say("Desculpe, não entendi.")
        except Exception as x: #Crash handler
            from MaidUtils.init import crash_handler #Importando crash handler
            crash_handler.Handle(x, 'Execução') #Executando

###################################
###Esta é a parte onde a maid e iniciada
###################################

if __name__ == "__main__": #Processo de inicialização da maid
    try:                                         #Pega exceções na inicialização da maid
        import sys
        sys.stdout.write("\x1b]2;Maid\x07")
        
        from colorama import Fore, init
        init()

        from config import analyze_conditions    #Executando o config.py e analizando
        analyze_conditions()                     #Se as configs existem

        import pyfiglet                          #Coisas para deixar o terminal da maid bonito (eu n vou fazer uma gui pra ela)
        pyfiglet.print_figlet("Maid")            #Escreve "maid" de uma forma muito foda
        print("Programado por: Polarfill (@polarfill / https://github.com/PolarFill)")

        from MaidUtils.init import update
        update.Check()                           #Checa updates, e mostra se tiver algum mostra no terminal

        print("#####################################################")
        print(Fore.CYAN + "Carregando a maid...")
        
        from MaidUtils.init import check_connection    #Checando se há uma conexão com a internet
        check_connection.Connection()
        
        from MaidUtils.init import initcheck           
        initcheck.Init()                               #Checa algumas configurações principais
                                        
        print("Diga o comando que deseja executar" + Fore.RESET)
        
    except Exception as x:
            from MaidUtils.init import crash_handler #Importando crash handler
            crash_handler.Handle(x, 'Inicialização') #Executando
        
    eternal_input()                                #Usuario é jogado para a função que analisa inputs, onde a magica acontece.
        