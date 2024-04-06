entry = input()

entry_list = entry.split()
opposite_list = []

for number in entry_list:
    opposite_number = int(number) * -1
    opposite_list.append(opposite_number)

print(opposite_list)
