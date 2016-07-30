# will ask for monthly statistics

# list of months
months = ["Janurary", "Feburary", "March", "April", "May",
         "June", "July", "Augest", "September", "October",
         "November", "December"]

# ask for statistic for each month
def askMonth(current_month):
    """current month will be items from the list 'months'"""
    while True:
        ask_msg = ("[Enter Hours of Daylight for " + str(current_month) + "]: ")
        month = input(ask_msg)
        try:
            month = float(month)
            break
        except:
            input("That's not a valid number, try again\n")
    return month

# takes the list of stats from each month, and find the average of it
def calcAverage(list_in):
    list_sum = 0
    for i in list_in:
        list_sum += float(i)
    list_average = list_sum / 12
    return list_average

# extracts each and every item from 'months' and input them into the function askMonth()
month_list = []
for month in months:
    month_list.append(askMonth(month))

# prints out the average, max and min from the list of stats
print("\n\nAverage Day Time:", "{:.2f}".format(calcAverage(month_list)))
print("Year Maximum:", max(month_list))
print("Year Minimum:", min(month_list))
