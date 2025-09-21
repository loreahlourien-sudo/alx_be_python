Task = input("name of the task ")
Priority = input("task priority(high,medium,low)")
Time_Bound = input("is the task time bound (yes,no)")
match priority and time_bound:
case priority =="high" and time_bound =="yes":
 print( task,"is a high priority task that requires immediate attention today!")
case priority == "high" and time_bound == "no": 
 print(task,"is a high priority")
case priority == "medium" and time_bound == "yes":
 print(task, "is a medium priority task that requires  attention!")
case priority == "medium" and time_bound == "no":
 print(task"is a medium priority")
case priority == "low" and time_bound =="yes":
 print(task, "is a low priority task.")
case priority == "low" and time_bound == "no":
   print (task,"is a low priority task.")
   
