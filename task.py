import numpy as np


"""Creates a task object. To create an object: import task, and call task.Task("activity", "occurrence", "describe")
where occurrence is either "daily" or "weekly" (other gives time = 0)
    """
class Task():
    def __init__(self, activityName, occurrence, length): #, describe: str = ""):
        # Task/Ticket Properties
        # Tasks include: Activity Name, Description, Times, Completed(boolean)
        self.activity = activityName
        #self.description = describe
        self.completed = False
        self.time = occurrence
        self.distance = length
            
        self.doing = np.full(len(self.time), False)
    
    # Determines whether the task was completed or not
    def isFinished(self):
        finished = False
        for i in range(len(self.doing)):
            if self.doing[i]:
                finished = True
            else:
                finished = False
                break
        
        return finished
           
    

# Our app suggested ones (suggest 1 per day)

# User inputed ones (these show up in the training plan 
# every____(time period user chose, e.g. run 2 times per week doesn't show up until next week when completed))



# Check off a task

# How regularly it pops up (daily, weekly, days of the week, monthly)