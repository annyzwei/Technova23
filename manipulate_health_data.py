import xlwings as xw
import os
from pprint import pprint
from datetime import datetime

ws = xw.Book("Health Data Technova.xlsx").sheets['Workout Data']

workout_data = ws.range("A1").expand().value
rows = len(workout_data)
columns = len(workout_data[0])

# inputs the data point for the given entry (ex. putting StepCount into pos[0])
def input_stat(wrkout_entry, type, value):
    value = round(value, 2)
    if (type == "HKQuantityTypeIdentifierStepCount"):
        wrkout_entry[1] = value
    elif (type == "HKQuantityTypeIdentifierActiveEnergyBurned"):
        wrkout_entry[2] = value
    elif (type == "HKQuantityTypeIdentifierRunningSpeed"):
        wrkout_entry[3] = value
    elif (type == "HKQuantityTypeIdentifierDistanceWalkingRunning"):
        wrkout_entry[4] = value
    elif (type == "HKQuantityTypeIdentifierHeartRate"):
        wrkout_entry[5] = value
    else:
        print("There are other workout stats!")

wrkout_collection = []
wrkout_collection.append(['date/time', 'Step Count', 'Energy Burned (cal)', 'Running Speed', 'Distance (km)', 'Heart Rate', 'Time (min)'])
date = ""
end_date = ""
length = ""
wrkout_entry = [0] * 7
activity_time = 0
for entry in workout_data[1:]:
    if entry[1] != date:
        if activity_time != 0 and wrkout_entry[4]:
            wrkout_entry[3] = round(wrkout_entry[4] / (activity_time / 60), 2)
        wrkout_collection.append(wrkout_entry)
        date = entry[1]
        end_date = entry[2]
        start_time = datetime.strptime(date[11:19], "%H:%M:%S")
        end_time = datetime.strptime(end_date[11:19], "%H:%M:%S")

        activity_time = ((end_time - start_time).total_seconds() / 60)
        activity_time = round(activity_time, 2)
        wrkout_entry = [0] * 7
        wrkout_entry[0] = date
        wrkout_entry[6] = activity_time
    
    if entry[3] == None:
        val = 0
    else:
        val = float(entry[3])
    input_stat(wrkout_entry, entry[0], val)

wrkout_collection.pop(1)

pprint(wrkout_collection)

