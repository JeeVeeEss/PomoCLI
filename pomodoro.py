# PomoCLI
import os
import time
from colorama import Fore, Back, Style
import random
import sys
from win10toast import ToastNotifier 


class PomoCli:
    tasks = []
    toast = ToastNotifier()
    banner = """
                                                █████████   █████       █████
                                                ███░░░░░███ ░░███       ░░███ 
    ████████   ██████  █████████████    ██████  ███     ░░░  ░███        ░███ 
   ░░███░░███ ███░░███░░███░░███░░███  ███░░███░███          ░███        ░███ 
    ░███ ░███░███ ░███ ░███ ░███ ░███ ░███ ░███░███          ░███        ░███ 
    ░███ ░███░███ ░███ ░███ ░███ ░███ ░███ ░███░░███     ███ ░███      █ ░███ 
    ░███████ ░░██████  █████░███ █████░░██████  ░░█████████  ███████████ █████
    ░███░░░   ░░░░░░  ░░░░░ ░░░ ░░░░░  ░░░░░░    ░░░░░░░░░  ░░░░░░░░░░░ ░░░░░ 
    ░███                                                                      
    █████                                                                     
    ░░░░░

    Para gerenciar as tasks - "1"
    Para iniciar uma sessão Pomodoro - "2" 
    Para sair do programa - "Sair" ou "sair"                                                      
    """
    def __init__(self):
        os.system('cls')
        self.main()
        
        
    def main(self): ## Inicializador 
        os.system('cls')
        print(self.banner)
        print('   ', self.tasks)
        sys.stdout.write('    '+Fore.GREEN + '@(Vamos Lá)  '+ Style.RESET_ALL + '-  ')
        time.sleep(0.85)
        self.inicio = str(input('Escolho: '))
        self.GoOn()

    def GoOn(self): # Menu de Escolhas do Gerenciador de Tasks.
        try:
            if self.inicio == '1':
                print(''' 
        1. Adicionar Tasks.
        2. Limpar Tasks.
        3. Remover Task.
        4. Mostrar Tasks.
    ''')
                options = int(input('Opções: '))
            
                if options == 1: # Opção *1*: Adicionar Tasks.
                    new = str(input("Nome da Task: "))
                    self.tasks.append(new)
                    print(f'{i, i in self.tasks}\n')
                    time.sleep(1)
                    os.system('cls')
                    self.main()

                elif options == 2: # Opção *2*: Limpar todas as Tasks.
                    self.tasks = []
                    self.main()

                elif options == 3: # Opção *3*: Remover itens das Tasks por meio de índice.
                    item = int(input('Digite a posição da Task: '))
                    self.tasks.pop(item-1)
                    time.sleep(1)
                    print(self.tasks)
                    self.main()
                
                elif options == 4:
                    self.main()
                else: 
                    raise Exception
                
            elif self.inicio == '2': # Parte do Timer:   
                        
                timer = int(input(Back.GREEN+'Selecione quanto tempo deseja estudar: ' +Style.RESET_ALL))
                timer = timer *60
                TIMER = timer
                BAR = chr(9608)
                for i in range(timer): # Barra de progresso(porcentagem)
                    print(f"               |      {random.choice(['!','@','#','#','$','%'])}              " + f"[{(i/TIMER)*100:.2f}%]" + f"              {random.choice(['!','@','#','#','$','%'])}           |")
                    timer = timer - 1
                    time.sleep(1)
                    os.system('cls')
                    print(Fore.GREEN + self.banner + Style.RESET_ALL)
            
                    
                self.toast.show_toast(title='SESSÃO CONCLUÍDA!',msg=f"Tempo de estudo: {timer/60} minutos!", duration=10) # Envia a notificação.
                os.system('cls') 
                self.main() # Fim do Timer

            elif self.inicio in ['sair', 'Sair', 'leave', 'SAIR', 'exit', 'Exit']: # Função para sair do programa.
                os.system('cls')
                KeyboardInterrupt    
            else:
                raise Exception
        except Exception as e:
            print('Try Again!')
            time.sleep(0.30)
            os.system('cls')
            print(self.banner)
            self.main()
            

             

if __name__ == '__main__':
    a = PomoCli()#.__init__()