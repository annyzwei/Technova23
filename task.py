
class Task():
    def __init__(self, activityName, occurrence, describe: str = ""):
        # Task/Ticket Properties
        # Tasks include: Activity Name, Description, Times, Completed(boolean)
        self.activity = activityName
        self.description = describe
        self.completed = False
        
        if occurrence == "daily":
            self.time = 7
        elif occurrence == "weekly":
            self.time = 1
        else:
            self.time = 0
           
    

# Our app suggested ones (suggest 1 per day)

# User inputed ones (these show up in the training plan 
# every____(time period user chose, e.g. run 2 times per week doesn't show up until next week when completed))



# Check off a task

# How regularly it pops up (daily, weekly, days of the week, monthly)