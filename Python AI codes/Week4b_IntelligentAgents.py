import random
import time
class Environment(object):
    def __init__(self):
        self.mode = ['T', 'L']
        self.locationCondition = {'A': '0', 'B': '0'}
        self.cleaningmethod = {'A': 'T', 'B': 'T'}
	    # randomize conditions 
        self.locationCondition['A'] = random.randint(0, 1)
        self.locationCondition['B'] = random.randint(0, 1)
        self.cleaningmethod['A'] = random.choice(self.mode)
        self.cleaningmethod['B'] = random.choice(self.mode)
        # instantiate locations and conditions
        # 0 indicates Clean and 1 indicates Dirty
        self.Location=['A','B']
        
        # place vacuum at random location
        self.vacuumLocation = random.choice(self.Location)



class MyAgent(Environment):
   def __init__(self, Environment):
        # randomize conditions 
        print (Environment.locationCondition)
        print (Environment.cleaningmethod)
        print ("Vacuum is randomly placed at Location.", Environment.vacuumLocation)
        # and Location is Dirty.
        count=0
        n=0
        while count<2:
            if Environment.locationCondition[Environment.vacuumLocation] == 1 :
                if Environment.cleaningmethod[Environment.vacuumLocation] == "T":
                    Environment.cleaningmethod[Environment.vacuumLocation] = "L"
                 
                else:
                    Environment.cleaningmethod[Environment.vacuumLocation] = "T"
                Environment.locationCondition[Environment.vacuumLocation] = 0;
                print (Environment.vacuumLocation,"has been Cleaned.")

                
            else:
                print (Environment.vacuumLocation," is Clean.")
            newIndex=Environment.Location.index(Environment.vacuumLocation)+1
            if newIndex == 2:
                newIndex=0
            Environment.vacuumLocation=Environment.Location[newIndex]  
            count+=1    

        # done cleaning
        print (Environment.locationCondition)
        print (Environment.cleaningmethod)
x = 0
while x<7:
 time.sleep(2)
 theEnvironment = Environment()
 theVacuum = MyAgent(theEnvironment)

 x = x+1



        
        