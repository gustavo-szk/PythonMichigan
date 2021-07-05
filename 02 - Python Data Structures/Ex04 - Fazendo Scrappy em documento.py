# 7.2 Write a program that prompts for a file name, 
# then opens that file and reads through the file, 
# looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point 
# values from each of the lines and compute the average 
# of those values and produce an output as shown below. 
# Do not use the sum() function or a variable named sum in your solution.
# 3You can download the sample data at http://www.py4e.com/code3/mbox-short.txt 
# when you are testing below enter mbox-short.txt as the file name.

fh = open('mbox-short.txt')
nv = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    n = float(line[20:])
    nv = n+nv
    count = count + 1
    
media = nv / count

print("Average spam confidence:", media)
