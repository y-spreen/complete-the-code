link = "https://dbrand.com/%s4726%s%s%s2974%s%s"


numbers = "0123456789"

# https://dbrand.com/ (5,7) 4 7 2 6 * *         * 2 9 7 4 (0-7) *
firstchar = "57"
secondchar = numbers
thirdchar = numbers
fourtchar = numbers
fivechar = "01234567"
sixchar = numbers
startpoint = 80000

# new
link = "https://dbrand.com/%s4726%s%s%s6974%s%s"

# https://dbrand.com/ (5-7) 4 7 2 6 * *         4 6 9 7 4 (5-7) *
firstchar = "567"
secondchar = numbers
thirdchar = numbers
fourtchar = "4"
fivechar = "567"
sixchar = numbers
startpoint = 0

# newer

# https://dbrand.com/ (5-7) 4 7 2 6 * * (0-3,5-9) 6 9 7 4 (6,7) *
firstchar = "567"
secondchar = numbers
thirdchar = numbers
fourtchar = "012356789"  # no 4
fivechar = "67"
sixchar = numbers
startpoint = 0

count = 0
outstring = ""
for six in sixchar:
    for five in fivechar:
        for four in fourtchar:
            for three in thirdchar:
                for two in secondchar:
                    for one in firstchar:
                        count += 1
                        if count >= startpoint:
                            l = link % (one, two, three, four, five, six)
                            outstring += l + "\n"

with open("runfile.txt", "w") as f:
    f.write(outstring)

