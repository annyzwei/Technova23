import numpy as np


"""Creates a task object. To create an object: import task, and call task.Task("activity", "occurrence", "describe")
where occurrence is either "daily" or "weekly" (other gives time = 0)
    """
class Task():
    def __init__(self, activityName, countdown, length): #, describe: str = ""):
        # Task/Ticket Properties
        # Tasks include: Activity Name, Description, Days until completion, Completed(boolean)
        self.activity = activityName
        #self.description = describe
        self.completed = False
        self.finishedInTime = False
        self.time = countdown
        self.distance = length
        
    def dayPassed(self):
        if self.time > 0:
            self.time -= 1
            
        # Future changes: once it reaches -5, get rid of it
    
    def isFinished(self):
        return self.completed
    
    def completeTask(self):
        self.completed = True
        
        if self.time > 0:
            self.finishedInTime = True
           
    def jsonable(self):
        return self.__dict__
    

# Our app suggested ones (suggest 1 per day)

# User inputed ones (these show up in the training plan 
# every____(time period user chose, e.g. run 2 times per week doesn't show up until next week when completed))



# Check off a task

# How regularly it pops up (daily, weekly, days of the week, monthly)