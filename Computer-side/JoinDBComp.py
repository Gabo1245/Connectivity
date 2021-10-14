from ProcessManager import ProcessManager
from FirebaseHandler import FirebaseHandler
import time

class JoinDBComp():
    
    def __init__(self):
        self.processmanager = ProcessManager()
        self.firebasehandler = FirebaseHandler()
    
    def execute(self):

        while True:
            self.firebasehandler.processListener()
            self.process = self.firebasehandler.getProcess()
            self.processmanager.runProcess(self.process)
            time.sleep(0.1)



    