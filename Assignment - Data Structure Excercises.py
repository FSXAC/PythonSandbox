import random;

#   EXCERCISE P1 Q1
def exp1q1_encouragement():
    encourage = ["kill youself!",
                 "you dishonored your family!",
                 "you are a disgrace! to the entire humanity",
                 "you are worthless!",
                 "no one likes you!"
                 "shut your computer down and go cry in the corner!"];
    if str(input("would you like an encouragement to brighten up your day? (y/n) ")).lower() == "y":
        print(random.choice(encourage));

#    EXCERCISE P1 Q2
def exp1q2_daysOfWeek():
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday",
                    "Friday", "Saturday", "Sunday"];
    while True:
        day_number = input(\
        """
[1] Monday
[2] Tuesday
[3] Wednesday
[4] Thursday
[5] Friday
[6] Saturday
[7] Sunday\n""");
        try:
            day_number = int(day_number);
            print("\n", days_of_week[day_number - 1]);
            break;
        except:
            None;

#   EXCERCISE P1 Q3
def exp1q3_stringSlice():
    q3_str = "bothering";
    print("\n\n", q3_str[0:4], "\n",
          q3_str[0:3], "\n",
          q3_str[0:6], "\n",
          q3_str[1:6], "\n",
          q3_str[2:5], "\n",
          q3_str[3:6], "\n",
          q3_str[5:9], "\n",
          q3_str[6:8]);

# EXCERCISE P2 Q1
def exp2q1_createList_daysOfWeek():
    """ Create a list of the days of the week. """;
    days = ["Monday", "Tuesday", "Wednesday", "Thursday",
                    "Friday", "Saturday", "Sunday"];

# EXCERCISE P2 Q2
def exp2q2_100():
    """ Create a string of 100 question marks. """;
    question_str = "?" * 100;

# EXCERCISE P2 Q3
def exp2q3_asterisks():
    """  With one line of code print out a row of 50 asterisks '*'. """;
    print("*" * 50);

# EXCERCISE P2 Q4
def exp2q4_testMarks():
    """ Create a list of 5 test marks entered by the user. """;
    mark_list = []
    for i in range(5):
        mark_list.append(int(input("Test mark for test", i + 1)));
    print(mark_list);

# EXCERCISE P3 Q1
def exp3q1_addFive():
    """ Create a list and write a function that will add 5 to every
    element in the list. """;
    number_list = [4, 8, 15, 16, 23, 42];
    for i in len(number_list):
        number_list[i - 1] += 5;
    print(number_list);

# EXCERCISE P3 Q2
def exp3q2_100randomgen():
    default_list = [];
    even_list = [];
    for i in range(100):
        default_list.append(random.randrange(0, 11));

    for j in default_list:
        if j % 2 == 0:
            even_list.append(j);

    print(even_list);

# EXCE
    
            
        
exp1q1_encouragement();
exp1q2_daysOfWeek();
exp1q3_stringSlice();
