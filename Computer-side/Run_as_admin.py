import ctypes, sys, os
from ctypes import windll
from win32comext.shell import shell


class RunasAdmin():
    def is_admin(self):
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    def runasadmin(self, process):
        """ Runs any cmd command as an admin"""
       
        
        shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+ process)
    

        

