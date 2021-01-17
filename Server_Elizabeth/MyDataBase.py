# ----------------------------------------------------------------- -----------------------------------------------------------------

import os
import sqlite3 as SQL

# ----------------------------------------------------------------- -----------------------------------------------------------------

class Profile:
    
    def __init__(self, Login, Pass, Name, Test1 ):

        self.Login  = Login
        self.Pass   = Pass
        self.Name   = Name
        self.Test1  = Test1

    def setLogin(self,value):   self.Login  = value
    def setPass(self,value):    self.Pass   = value
    def setName(self,value):    self.Name   = value
    def setTest1(self,value):   self.Test1  = value
 
    def getLogin(self):         return self.Login 
    def getPass(self):          return self.Pass  
    def getName(self):          return self.Name  
    def getTest1(self):         return self.Test1 

    def __str__(self): return "\nLogin: {}\nPass: {}\nName: {}\nTest1: {}\n".format(self.Login, self.Pass, self.Name, self.Test1)
   
 # ----------------------------------------------------------------- -----------------------------------------------------------------

class DataBaseProfile:
    
    # ----------------------------------------------------------------- 

    def __init__(self): self.ListProfile = []       

    # ----------------------------------------------------------------- 

    def addProfile(self,Login, Pass, Name, Test1):
        NewProfile = Profile(Login,Pass,Name,Test1)
        self.ListProfile.append(NewProfile)
    
    # ----------------------------------------------------------------- 

    def getListProfile(self):       return self.ListProfile

    def getLenProfiles(self):       return len(self.ListProfile)

    def findProfileID(self,ID):     return self.ListProfile[ID]

    # ----------------------------------------------------------------- 

    def Clear(self): self.ListProfile.clear(); print(" >>> Clear Data Base !!!")

    # ----------------------------------------------------------------- 

    def setLogin(self,ID,value):    self.ListProfile[ID].setLogin(value)
    def setPass(self,ID,value):     self.ListProfile[ID].setPass(value)
    def setName(self,ID,value):     self.ListProfile[ID].setName(value)
    def setTest1(self,ID,value):    self.ListProfile[ID].setTest1(value); print(self.ListProfile[ID])

    # ----------------------------------------------------------------- 

    def getLogin(self,ID):          return self.ListProfile[ID].getLogin()
    def getPass(self,ID):           return self.ListProfile[ID].getPass() 
    def getName(self,ID):           return self.ListProfile[ID].getName() 
    def getTest1(self,ID):          return self.ListProfile[ID].getTest1() 

    # ----------------------------------------------------------------- 

    def getIndexByLogin(self,Login):
        for ID in range(self.getLenProfiles()):
            if(self.ListProfile[ID].getLogin() == Login): return ID
        return False

    # ----------------------------------------------------------------- 

    def SaveDB(self,FileName):

        print(" >>> Save Data Base File: ",  FileName)

        
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), FileName)
        os.remove(path)

        
        MyDataBase = SQL.connect(FileName)
        SQLite = MyDataBase.cursor()

        
        SQLite.execute("""CREATE TABLE IF NOT EXISTS Profile (Login TEXT, Pass TEXT, Name TEXT, Test1 INT)""")

        
        MyDataBase.commit()

        
        MyProfile    = [ [
            self.ListProfile[I].getLogin(),
            self.ListProfile[I].getPass(),
            self.ListProfile[I].getName(), 
            self.ListProfile[I].getTest1()
            ] for I in range(len(self.ListProfile)) ]
        
        for ID in range(len(MyProfile)): 
            SQLite.execute(f"SELECT Login FROM Profile WHERE Login = '{MyProfile[ID][0]}'")
            if SQLite.fetchone() is None:
                print(" >>> Save Name Profile: ", MyProfile[ID][2])
                SQLite.execute(f"INSERT INTO Profile VALUES ( '{MyProfile[ID][0]}', '{MyProfile[ID][1]}', '{MyProfile[ID][2]}', {MyProfile[ID][3]})")
            MyDataBase.commit()

        
        print(" >>> Save Data Base Complete")
        MyDataBase.commit()

    # ----------------------------------------------------------------- 

    
    def LoadDB(self,FileName):

        print(" >>> Load Data Base File: ",  FileName)

        
        MyDataBase = SQL.connect(FileName)
        SQLite = MyDataBase.cursor()

        
        for ITEM in SQLite.execute("SELECT * FROM Profile"): 
            print(" >>> Load Name Profile: ", ITEM[2])
            self.addProfile(ITEM[0],ITEM[1],ITEM[2],ITEM[3]) 

        print(" >>> Load Data Base Complete")
    
    # ----------------------------------------------------------------- 
