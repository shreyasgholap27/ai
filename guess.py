low = 1
high = 100

attempts = 0

while low<=high:
    attempts+=1
    guess = (low+high)//2
    print(f"guess is{guess}")
    feedback = input("enter h for higher l for lower and c for correct")
    if feedback=="h":
        low=guess+1
    elif feedback=="l":
        high=guess-1
    elif feedback=="c":
        print("your no. is ",guess)
        break
    else:
        print("invalid input")
        
print("your attempt is",attempts)
        