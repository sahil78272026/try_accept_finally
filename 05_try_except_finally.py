try:
    i = int(input("Enter a number: "))
    c = 1/i
except Exception as e:
    print(e)
    exit()
finally:  # finally block will execute anyhow , even if we exit the program
    print("We are done")

print("Thanks for using the program")