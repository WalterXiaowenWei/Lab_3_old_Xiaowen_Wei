# 4. Time Calculator
# Write a program that asks the user to enter a number of seconds, and works as follows:
# • There are 60 seconds in a minute. If the number of seconds entered by the user is greater than or equal to 60,
#  the program should display the number of minutes in that many seconds.
# • There are 3,600 seconds in an hour. If the number of seconds entered by the user is greater than or equal to 3,600, 
# the program should display the number of hours in that many seconds.
# • There are 86,400 seconds in a day. If the number of seconds entered by the user is greater than or equal to 86,400, 
# the program should display the number of days in that many seconds.

x = 0 
while x < 1:
    time_input = float(input("Please enter a number of seconds: "))
    if time_input < 60:
        print("Time: ",time_input,"s")
    elif time_input >= 60 and time_input < 3600:
        print("Time: ",time_input/60,"min/mins")
    elif time_input >= 3600 and time_input < 86400:
        print("Time: ",time_input/3600,"hour/hours")
    elif time_input >= 86400:
        print("Time: ",time_input/86400,"day/days")
    else:
        print("Please input the correct time")
    

    
    