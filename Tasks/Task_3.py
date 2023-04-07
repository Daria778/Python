
firstCl = int(input('Enter the number of students in the first class: '))
secondCl = int(input('Enter the number of students in the second class: '))
thirdCl = int(input('Enter the number of students in the third class: '))
needDesks = (firstCl + secondCl + thirdCl) / 2
if(needDesks != 0) :
    needDesks += 1
    print(round(needDesks, 0))