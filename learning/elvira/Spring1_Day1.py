name= input('Enter your name:')
age_text=input('Enter your age:')
age_number=int(age_text)
if(age_number<18 and age_number>=0):
    print(f"{name} , You are not major yet!")
elif(age_number>=18 and age_number<=150):
     print(f"{name} , You are major!")
else:
     print(f'{name} It seems like your age is not correct')