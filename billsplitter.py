# write your code here
import random

print("Enter the number of friends joining (including you):")
friends_number = int(input())

if friends_number > 0:

    friends = {}
    friends_list = []
    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range(friends_number):
        friend_name = input()
        friends[friend_name] = 0
        friends_list.append(friend_name)

    print("Enter the total bill value:")
    final_bill = int(input())
    split_bill = round(final_bill / friends_number, 2)

    for friend in friends:
        friends[friend] = split_bill

    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    choice = input()

    if choice == 'Yes':
        lucky_one = random.choice(friends_list)
        print(lucky_one, "is the lucky one!")

        split_bill = round(final_bill / (friends_number - 1), 2)

        for friend in friends:
            friends[friend] = split_bill
        friends[lucky_one] = 0

    else:
        print("No one is going to be lucky")

    print(friends)
else:
    print("No one is joining for the party")
