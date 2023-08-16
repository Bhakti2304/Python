"""count days until deadline"""
import datetime

user_input=input("enter your goal with deadline\n")
input_list=user_input.split(":")

goal=input_list[0]
deadline=input_list[1]
print(input_list)

deadline_date=datetime.datetime.strptime(deadline,"%d.%m.%Y")
today_date=datetime.datetime.today()
#calculate how many days from now till deadline

time_till= deadline_date-today_date
print(f"Time remaining for your goal: {goal} is {time_till} hours")
