import sys

answer = ''  # Для ответа
answer2 = ''

n1 = int(sys.argv[1])
m1 = int(sys.argv[2])
n2 = int(sys.argv[3])
m2 = int(sys.argv[4])

number = 1
interval = []
intervals = []
for i in range(m1):
    if number > n1:
        number = 1
    interval.append(number)
    number += 1
intervals.append(interval)
answer += str(interval[0])

number2 = 1
interval2 = []
intervals2 = []
for i in range(m2):
    if number2 > n2:
        number2 = 1
    interval2.append(number2)
    number2 += 1
intervals2.append(interval2)
answer2 += str(interval2[0])

while intervals[-1][-1] != 1 or intervals2[-1][-1] != 1:
    if intervals[-1][-1] != 1:
        interval = []
        number = intervals[-1][-1]
        for i in range(m1):
            if number > n1:
                number = 1
            interval.append(number)
            number += 1
        intervals.append(interval)
        answer += str(interval[0])

    if intervals2[-1][-1] != 1:
        interval2 = []
        number2 = intervals2[-1][-1]
        for i in range(m2):
            if number2 > n2:
                number2 = 1
            interval2.append(number2)
            number2 += 1
        intervals2.append(interval2)
        answer2 += str(interval2[0])

print(answer + answer2)





