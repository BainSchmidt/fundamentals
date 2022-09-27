for i in range(151):
    print(i)

count = 5
while count <= 1000:
    print("looping - ", count)
    count += 5

for i in range(1, 101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

sum_odd = 0
for number in range(1,500001, 2):
    sum_odd = sum_odd + number
print(f"odd sum = {sum_odd}")

count = 2018
while count >= 0:
    print(count)
    count -= 4

low_num = 1
high_num = 9
mult = 3

for i in range(low_num, high_num + 1):
    if i % mult == 0:
        print(i)