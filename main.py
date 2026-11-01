from random import randint

secret = randint(1, 100)

attempt = 7


while True:
    try:
        number = int(input("enter a number: "))
    except ValueError:
        print("Please enter a number!")
        continue

    attempt -= 1

    if number == secret:
        print("Congratulations! You Won!","attempts:", attempt)
        break
    elif attempt == 0:
        print("Sorry, you lost!","attempts:", attempt)
        break
    elif number < secret:
        print("Too low!","attempts:", attempt)
    else:
        print("Too high!","attempts:", attempt)


print("Thank you for playing!" ,"secret:", secret)







