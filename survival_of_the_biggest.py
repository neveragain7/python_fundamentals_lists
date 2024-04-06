list_of_integers = input().split()
count_of_removals = int(input())

final_string = ""

for index in range(len(list_of_integers)):
    list_of_integers[index] = int(list_of_integers[index])

for count in range(count_of_removals):
    min_number = min(list_of_integers)
    list_of_integers.remove(min_number)

for index in range(len(list_of_integers)):
    list_of_integers[index] = str(list_of_integers[index])

print(", ".join(list_of_integers))
