#Initialize a dictionary to serve as a counter for each given range.
number_counter = {
         "1-10": 0,
         "11-20": 0,
         "21-30": 0,
         "31-40": 0,
         "41-50": 0         
}
#Start a loop that will ask the user to input numbers.

#Ask the user to input numbers from 1 to 50.
enter_number = int(input("Please enter a number from 1 to 50: "))
#Use an if statement to give a condition only numbers 1 to 50 are accepted.
if enter_number >= 1 and enter_number <= 50:  
        	
#Define each counter into 5 different ranges where each input will fall in.
      if enter_number <= 10 and enter_number >=1:
      	number_counter ["1-10"] += 1
      elif enter_number > 10 and enter_number <=20:
      	number_counter ["11-20"] += 1
      elif enter_number > 20 and enter_number <=30:
      	number_counter ["21-30"] += 1
      elif enter_number > 30 and enter_number <=40:
      	number_counter ["31-40"] += 1
      elif enter_number > 40 and enter_number <=50:
      	number_counter ["41-50"] += 1

#Use an else statement to print an error message when an input is invalid and break the loop.

#Print the counts for each interval defined.
print(number_counter)
