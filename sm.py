age=int(input("Enter your age:"))
income=int(input("Enter your annual income:"))
cast=input("enter your cast:")
if 18<=age<=25:

    if income<=300000:
        if cast=="open"or cast=="ST" or cast=="NT":

         print("you are eligible for scholarship")

        else:
           print("you are not eligible for scholarship")  

    else:   
       print("you are not eligible for scholarship")

else:
   print("you are not eligible for scholarship")
   