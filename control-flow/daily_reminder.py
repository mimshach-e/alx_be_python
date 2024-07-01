# Personal Daily Reminder

# Prompting for a Single Task:
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")


# Processing the Task Based on Priority and Time Sensitivity:
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a high priority task. Consider setting a time to complete it soon!")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task. You can work on it now or later")
        else:
            print(f"Note: '{task}' is a medium priority task. Find time to do it before it becomes too late!")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task that requires less attention!")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")                    
        
        


