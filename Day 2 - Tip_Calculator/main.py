#If the bill was $150.00, split between 5 people, with 12% tip. 
print("Welcome to the tip calculator")

bill = float(input("What is the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
no_of_people = int(input("How many people are splitting the bill? "))

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
each_person_pays = bill / no_of_people * 1.12
#final_amount = round(each_person_pays, 2)
final_amount = "{:.2f}".format(each_person_pays)

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
print(f"Each person should pay: ${final_amount}")
#Write your code below this line 👇