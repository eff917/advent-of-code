numbersdict = {}
prevnumber = None
with open('2020/dec15/input.txt', 'r') as infile:
    numbers = infile.readline().strip().split(',')
    numbers = [int(x) for x in numbers]
    prevnumber = numbers[-1]
    for turn, number in enumerate(numbers):
        if number not in numbersdict.keys():
            numbersdict[number] = [turn + 1]
        else:
            numbersdict[number].append(turn + 1)

# takes 12-13 minutes :)
for i in range(len(numbers) + 1,30000000 + 1):
    # print(numbersdict)
    if len(numbersdict[prevnumber]) == 1:
        numbersdict[0].append(i)
        prevnumber = 0
    else:
        prevnumber = numbersdict[prevnumber][-1] - numbersdict[prevnumber][-2]
        if prevnumber in numbersdict.keys():
            numbersdict[prevnumber].append(i)
        else:
            numbersdict[prevnumber] = [i]

        
        pass
    print(f"Turn {i}: number spoken was {prevnumber}")
print(prevnumber)