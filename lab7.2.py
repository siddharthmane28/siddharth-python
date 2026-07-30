print("***traffic signal rule***")
signal=input("Enter the signal colour:")

if signal =="red":
    print("action: stop")

elif signal =="yellow":
    print("action: wait")

elif signal =="green":
    print("action: Go")

else:
    print("invalid signal")            
