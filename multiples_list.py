factor = int(input())
count = int(input())

multiples_list = []

for number in range(1, count + 1):
    multiple = number * factor
    multiples_list.append(multiple)

print(multiples_list)
