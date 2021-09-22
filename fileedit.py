"""
Write a program that prompts for a file name, then opens that file and reads through the file,
looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines
and compute the average of those values and produce an output as shown below.
Do not use the sum() function or a variable named sum in your solution.


"""
#reading the file
file = input("Please enter file name: ")
datafile = open(file, "rt")
datafile.close

#counting the number of values in each line
count = 0
xlist = []
for line in datafile:
   if "X-DSPAM-Confidence" in line:
        count += 1 
        xlist.append(line)
print(count) 
#print(xlist) 

#splitting the value from the sring         
newlist = []
for x in xlist:
    newlist.append(x.strip().split(":"))
#print(newlist)    
 
#converting the values from string and summing up    
total = 0
for new_line in newlist:
    total += float(new_line[1])
print(total)    

average = total/count

print("The average of X-DSPAM-Confidence values in this file is {:.4f}".format(average))