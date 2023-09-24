import numpy as np
import task
import json

class User():
    #goals -> list of task objects
    def __init__(self, user_dict): #, describe: str = ""):


        self.exp = int(user_dict['exp'])
        self.strength = int(user_dict['strength'])
        self.speed = int(user_dict["speed"])
        self.health = int(user_dict["health"])
        self.mana = int(user_dict["mana"])
        self.stamina = int(user_dict["stamina"])
        self.goals = []
        for i in range(len(user_dict['goals'])):
            self.goals.append(task.Task(user_dict['goals'][i]["activity"], 
                                        int(user_dict['goals'][i]["time"]),
                                        int(user_dict['goals'][i]["distance"])))
    def jsonable(self):
        return self.__dict__

    

# Our app suggested ones (suggest 1 per day)

# User inputed ones (these show up in the training plan 
# every____(time period user chose, e.g. run 2 times per week doesn't show up until next week when completed))



# Check off a task

# How regularly it pops up (daily, weekly, days of the week, monthly)