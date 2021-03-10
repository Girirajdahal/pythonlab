#WAP to convert secondws into day hour and minutes
seconds=int(input("Enter the number of seconds"))
minutes= seconds/60
hours= seconds/(60*60)
days=seconds/(60*60*24)
print(f"Converted number of minutes={minutes}")
print(f"converted number of hours={hours}")
print(f"converted number of dayss={days}")
