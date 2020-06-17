"""
Author  : Vivek Shinde
Date    : 17/06/2020
purpose : Practice problem solving
code    : Funny names

"""

if __name__ == '__main__':
    names_list = []
    number_of_friends = int(input("Enter number of friends : "))
    for i in range(number_of_friends):
        name_of_friends = input("Enter name of Friend : ")
        names_list.append(name_of_friends)
    # print(names_list)

    new_list = []

    for x in names_list:
        name_surname = x.split()
        new_list.append(name_surname)
    # print(new_list)

    for y in range(len(new_list)):
        temp = new_list[y][1]  # value of y starts from [0,1,2,3...len(new_list)]
        new_list[y][1] = new_list[number_of_friends - 1][1]
        new_list[number_of_friends - 1][1] = temp
        # print(new_list) # to understand how loop works
    # print(new_list)

    print('\nThe funnny names are :')
    # to combine new list
    for combine_name in new_list:
        join = " ".join(combine_name)
        print(f'\"{join}\"')
