# The first day of Sprint 1

**Date**: 13 April 2026
**Objective**: For the first day of Sprint 1 I should study :
- Variables and managing variables; 
- Primitive variable type ;
- Conditions & loops ;

## Variables

### What is a variable?
A **Variable** is a labeled storage box in your computer's memory. To assign a value to a variable we use the equals sign (=) , so we can assign :
- Integers (whole numbers) : x=7;
- Floats (Decimam numbers) : y=3.203 . These numbers are also called 'Floating point' numbers ;
- Strings (text) : name="BELLA ATENTSA";

### How to display a variable ? 
To display a variable on screen we use the function **print()**. 
Example: print(x) print(y) print(name) print(x,y,name)

### Shortcuts and Styling 
In python we have different types of assignment : 
- multiple assignment : which is used to assign the exact starting value for different boxes . Example : a=b=7
- parallel assignment : which is used to assign multiple variable once in the same line . Example : x,y=4,2

### Decimal formatting 
When you display a decimal number you can choose the number of decimal you want to show on to the screen using the format : '%.nf'%VarName where n is the number of decimal you want to show . We should notice that Python does not just truncate the value but it rounds it . 

### Other formats
- **%i** for formatting a value on to an interger or a whole number
- **%s** for formatting a value on to a string 

### Creating variables from others variable
In python , that's the common engine , we create a variable using others existing variables . 
Example: x=y+z u=2*y

### naming a variable 
The name of a variable always start either of a letter or an underscore and after that we can put both numbers and letters . Yet we should notice that only the underscore character is allow in python for naming a variable others are totally proscrited .
For the standard we usually write our variable with a lowercase format and when the variable is formed by multiple words , we can use either the **Camel case format** ( example : myVariable) or the **Snake case format** (example: my_variable).

### creating a variable using a sequence of value 
To do that we use the function **range()** which is the function for generating numbers in python.
Example: 
- x=range(10) it will create a list of numbers starting from 0 to 9 ;
- y=range(2,10) here we precise the start and the stop so it will go from 2 to 9 ;
- z=range(2,10,2) here we precise the start, the stop and the step 
To display those variables we cannot just type print(x) for example we you use tips like list or tuple .
Example: print(list(x)) print(tuple(y))

### Data Type and Dynamic Typing 
In python like other languages, variable has a type , a nature which can be integer, float, bool, string and so on. However , in Python we are free to specify or not the type of a variable while creating it for the first time. we can simply assign a value to a variable an python will typing the variable by itself : that's **dynamic typing** . But becarefull , because if you write something wrong that can cheat Python in typing you may have what you don't expect .Example : write x="2" instead of x=2 or write x=2. instead of x=2. So to see the type of a value we use the function **type()**.

### Converting Type
In Python, we can cast a string to an integer using int() , a string to a float using float() and any number to a string using str(). We should also becarefull cause if you use these functions badly , Python will generate a ValueError. 
To cast a text into a number we should be sure that the text represent only one number and does not contain something else. 
We use str() usually when you want to display or print within a text a number cause in python we don't simply add a number in text that will generate a typeError . 

### Method related to variables

- the function **dir()** is used to display what a variable which is here an object knows how to do. 
- the function **help()** is used to show how to use a special function of an object.

## Operators
### Arithmetic operators

- **/** that is the normal division we already know.
- **//** that is a division which gives us the result only the whole part of the result: it's called **floor Division**.
- **%** that's the modulo, which gives us the remainder of a floor division.
- Power(**) that's used for exponent. For example : x**2 which is x squared.
- the shorcuts : **+= and -=** 

### Logical operators

- **=** which is for assignment
- **==** which is for comparison
- **>** which means greater than
- **<** which means less than
- **<=** less or equal
- **>=** great or equal
- **and/&** and 
- **or/|** or
- **not/~** not
- **is**
- **in**
- **XOR/^**
- **is not**
- **not in**
- **<</>>**

## Conditions
if, elif, if not, nesting if, else.
sometimes for readability we have to define the condition out of the if .

## Loops
We have the **While** loop and the **for** loop.
There is also a difference between **break** and **continue** which is : when we use break, unless the sequence isn't at its end , if it hits the break instruction , we directly stop the loop and go to the code under. Instead , when we use continue the program just skip the value on which we reach the condition where we define continue and the loop continue its iterations.

## Practical
### Exercise 1: The Transaction Classifier (Data Cleaning)

In a real pipeline, you often get a mix of good and bad data. You need to "clean" a list of transactions.

The Goal: Write a program that takes a list of mixed values and:

    Skips any data that is not a number (use type() is not int and type() is not float).

    Labels numbers as "Deposit" (positive) or "Withdrawal" (negative).

    Calculates the Final Balance at the end.

The Data:
raw_data = [150.0, "ERROR_404", -20.50, 300, "MISSING_DATA", -100, 50.75]

#### My code 
raw_data=[150.0, "ERROR_404", -20.50, 300, "MISSING_DATA", -100, 50.75]
Final_balance=0
for i in raw_data:
    condition=(type(i) is not int and type(i) is not float)
    if condition:
        continue

    if(i>0):
        print('Deposit :' +str(i))
    else:
        print("Withdrawal :"+str(i))
    Final_balance+=i
print(Final_balance)

### Exercise 2:The Daily Withdrawal Limit (Loop Control)

Banks often have a security limit. If a customer tries to withdraw too much in one day, the system must stop them.

The Goal:

    Set a DAILY_LIMIT = 500.

    Loop through a list of withdrawal attempts: attempts = [100, 250, 50, 300, 40].

    Keep a "Running Total" of how much they have withdrawn so far.

    Before each withdrawal, check: If this next withdrawal will put them over the 500 limit, print a warning and use break to stop processing any more attempts.

    If it's safe, add it to the total and print "Transaction Approved. New Total: [X]".
    
#### My code 
daily_limit=500
attempts = [100, 250, 50, 300, 40]
running_total=0
for i in attempts :
    condition=(running_total+i >500)
    if condition:
        print(' Warning: This Withdraw('+str(i)+')will go over the daily limit. You still have the possibility to withdraw only:'+str(500-running_total))
        break
    running_total+=i
    print('Transaction approved for :'+str(i)+ 'and the new running total is :'+str(running_total) )

### Exercise 3: The Account "Masker" (String Logic)

For privacy (GDPR), banks often hide part of an account number, like: ****-****-1234.

The Goal:

    Create a variable account_number = "5432-8765-1234-9988".

    Use a for loop to look at every character in the string.

    If the character is a digit AND it is not one of the last 4 digits, print a *.

    If it is a dash - or one of the last 4 digits, print the actual character.

        Hint: To check for the last 4 digits, you could use a counter variable that increments in the loop.

#### My code 
account_number = "5432-8765-1234-9988"
len_account_number=0
for i in account_number:
    if(i!='-'):
        len_account_number+=1
    else:
        continue
len_minus=len_account_number-4
count=0
for i in account_number:
    if (count<len_minus and i!='-'):
        print('*',end='')
        count+=1
    else:
        print(i, end="")
print("")

- **Note Well**: to obligate python to stay in the same line , we use the function **end=''**

### Exercise 4: Interest Calculator (Math + Formatting)

Write a program that calculates how a savings account grows over 12 months.

The Goal:

    Start with balance = 1000.

    Set a monthly_interest_rate = 0.005 (0.5%).

    Use for i in range(1, 13): to represent 12 months.

    In each loop, add the interest to the balance (balance += balance * monthly_interest_rate).

    Print the balance for each month formatted to 2 decimal places (like you saw in the book!)
    
#### My code
balance=1000
months=["January","February", "March", "April", "May", "June","July","August","September","October","November","December"]
monthly_interest_rate=0.005
for i in range(1, 13):
    balance+= balance*0.005
    print(f'for the month:{months[i-1]} the balance is : {'%.2f'%balance}')
print(f'the total balance for this year is : {'%.2f'%balance}')


### Exercise for this day
for this day the exercise is to make a program which ask for user's information(name, age) and tell if he is major or minor using what we saw untill now. And to see what i've done please check the **learning/elvira/Sprint1_Day1.py** file .
