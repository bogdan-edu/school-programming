sorted_list = [3, 9, 12, 22, 23, 27, 28, 39, 45, 50, 58, 60, 61, 73, 76, 85, 89, 92, 94, 99]

quest = 85

midpoint = len(sorted_list) // 2
start = 0
end = len(sorted_list) - 1

while sorted_list[midpoint] != quest and start <= end:
    if quest > sorted_list[midpoint]:
        start = midpoint + 1
    else:
        end = midpoint - 1
    midpoint = (start + end) // 2

if start > end:
    print("Такого значення немає")
else:
    print("Значення знаходиться на позиції: ", midpoint)
