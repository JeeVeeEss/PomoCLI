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
    """
    def __init__(self):
        os.system('cls')
        self.main()
        
        
    def main(self): ## Inicializador 
        os.system('cls')
        print(self.banner)
        print('  ', self.tasks)
        sys.stdout.write(Fore.GREEN + '@(Vamos Lá) - '+ Style.RESET_ALL)
        time.sleep(0.85)
        self.inicio = str(input('Escolho: '))
        self.GoOn()

    def GoOn(self):
        try:
            if self.inicio == '1':
                print(''' 
        1. Adicionar Tasks.
        2. Limpar Tasks.
        3. Remover Task.
        4. Mostrar Tasks.
    ''')
                options = int(input('Opções: '))
            
                if options == 1:
                    new = str(input("Nome da Task: "))
                    self.tasks.append(new)
                    print(f'{self.tasks}')
                    time.sleep(1)
                    os.system('cls')
                    self.main()

                elif options == 2:
                    self.tasks = []
                    self.main()

                elif options == 3:
                    item = int(input('Digite a posição da Task: '))
                    self.tasks.pop(item-1)
                    time.sleep(1)
                    print(self.tasks)
                    self.main()
                
                elif options == 4:
                    self.main()
                else: 
                    raise Exception
                
            elif self.inicio == '2':    
                        
                timer = int(input(Back.GREEN+'Selecione quanto tempo deseja estudar: ' +Style.RESET_ALL))
                timer = timer *60
                for i in range(timer):
                    print(f"               |      {random.choice(['!','@','#','#','$','%'])}                " + str(timer) + f"              {random.choice(['!','@','#','#','$','%'])}           |")
                    timer = timer - 1
                    time.sleep(1)
                    os.system('cls')
                    print(Fore.GREEN + self.banner + Style.RESET_ALL)
            
                    
                self.toast.show_toast(title='POMODORO SESSION!',msg="YOU DONE IT", duration=10)
                os.system('cls')
                self.main()

            elif self.inicio in ['sair', 'Sair', 'leave', 'SAIR', 'exit', 'Exit']:
                os.system('cls')
                KeyboardInterrupt    
            else:
                raise Exception
        except Exception as e:
            print('Try Again!')
            os.system('cls')
            print(self.banner)
            self.GoOn()

             

if __name__ == '__main__':
    a = PomoCli()#.__init__()