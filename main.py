# numbers = [1,2,3,4,4,5,5,6]

# unique_list = list(set(numbers))

# print(unique_list)

#for loop

numbers = [1,2,3,4,5,6,7,8,9]

for num in numbers:
    if num %2 == 0:
        print(num)



first_name = "Blend"

for char in first_name:
    print(char)

dictonarie_names = {"Blend": 4, "Suela": 5, "Darsej": 1, "Leoni":3}
total_sum = 0

for vlera in dictonarie_names.values():
    print(vlera)
    total_sum +=vlera
    print("Shuma totale eshte:", total_sum)

for qelsat in dictonarie_names.keys():
    print(qelsat)

for i in range(1,10):
    print(i)

numrat = [1,42,5,21,4,5,67,12]
largest_num = numrat[0] #1

for num in numrat:
    if num > largest_num:
        largest_num = num

print(largest_num)

count = 0

while count <= 5:
    print(count)
    count += 1


