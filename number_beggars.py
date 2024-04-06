list_of_integers = input().split(", ")
count_of_beggars = int(input())

for index in range(len(list_of_integers)):
    list_of_integers[index] = int(list_of_integers[index])

beggar_list = []

for beggar in range(1, count_of_beggars + 1):
    beggar_total = 0
    for index in range(beggar, len(list_of_integers) + 1, count_of_beggars):
        beggar_total += list_of_integers[index - 1]
    beggar_list.append(beggar_total)

print(beggar_list)
