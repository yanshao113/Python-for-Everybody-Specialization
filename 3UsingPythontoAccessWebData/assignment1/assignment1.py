import re

txt = open("py4e-data.dr-chuck.net_regex_sum_1718580.txt")
numlist = []
for line in txt:
    line = line.rstrip()
    nums = re.findall("[0-9]+", line)
    if len(nums) <= 0:
        continue
    numlist.extend(nums)
Sum = 0
for i in numlist:
    Sum = int(i) + Sum

print(Sum)
