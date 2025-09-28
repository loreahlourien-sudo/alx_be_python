Task = input("name of the task ")
Priority = input("task priority(high,medium,low)")
Time_Bound = input("is the task time bound (yes,no)")
match Priority and Time_Bound:
case Priority =="high" and Time_Bound =="yes":
 print( Task,"is a high priority task that requires immediate attention today!")
case Priority == "high" and Time_Bound == "no": 
 print(Task,"is a high priority")
case Priority == "medium" and Time_Bound == "yes":
 print(Task, "is a medium priority task that requires  attention!")
case Priority == "medium" and Time_Bound == "no":
 print(Task"is a medium priority")
case Priority == "low" and Time_Bound =="yes":
 print(Task, "is a low priority task.")
case Priority == "low" and Time_Bound == "no":
   print (Task,"is a low priority task.")
   
