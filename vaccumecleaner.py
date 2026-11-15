environment = {"a":"clean","b":"dirty"}

position = "a"

while "dirty" in environment.values():
    if environment[position]=="dirty":
        print("action suck")
        environment[position]="clean"
    elif position == "a":
        print("move right")
        position = "b"
    else:
        print('move left')
        position= "a"
        
        

print("Final Room Status:", environment)
print("All rooms are clean!")

    
    