# Helen Li
# April 29, 2015
# Assignment #9

delete_count = 0 # count unusable lines
score = 0

students = [] # create list of student (IDs)
scores = [] # record scores of all students
scores_sorted = [] # sort scores to find median
uniquescores = [] # for mode
uniquescorescount = [] # for mode
uniquescoresmode = [] # if more than one mode

answerkey = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"

answerkeylist = answerkey.split(",")

while True:
    filename = input("Enter a class file to grade (i.e. class1 for class1.txt): ")

    try:
        myfile = open(filename+".txt", "r")
        break

    except:
        print ("File cannot be found.")
    
alldata = myfile.read()

myfile.close()

studentdata = alldata.split("\n")

for record in studentdata:
    splitrecord = record.split(',')
    # delete line if not usable
    if len(splitrecord) < 26 or len(splitrecord) > 26:
        del splitrecord
        delete_count += 1
    else:
        for a in range(0, len(splitrecord)-1):
            # add 4 if correct, take 1 away if wrong, nothing for blanks
            if splitrecord[a+1] == answerkeylist[a]:
                score += 4
            else:
                if splitrecord[a+1] == '':
                    score += 0
                else:
                    score -= 1

        students.append(splitrecord[0])
        scores.append(score)
        scores_sorted.append(score)
        score = 0
        
def median():
    scores_sorted.sort()
    if len(scores_sorted) % 2 == 0: # if even number of scores
        mid = len(scores_sorted)//2
        b = (scores_sorted[mid-1] + scores_sorted[mid])//2
        return b
    else:
        mid2 = len(scores_sorted)//2
        c = scores_sorted[mid2]
        return c

def mode():
    f = 1

    for d in scores:
        if d not in uniquescores:
            uniquescores.append(d)
            uniquescorescount.append(f)
        else:
            e = uniquescores.index(d)
            uniquescorescount[e] += 1

    g = max(uniquescorescount)
    while g in uniquescorescount:
        h = uniquescorescount.index(g)
        uniquescoresmode.append(uniquescores[h])
        del uniquescorescount[h]
        del uniquescores[h]

y = median()
mode()

print ()
print ("Grade Summary:")
print ("Total Students:", len(studentdata)-delete_count)
print ("Unusable lines in the file:", delete_count)
print ("Highest score:", max(scores))
print ("Lowest score:", min(scores))
print ("Mean score:", format((sum(scores)/len(scores)), ".2f"))
print ("Median score:", y)
print ("Mode: ", end="")
# print all modes
for j in uniquescoresmode:
    print (j, end=" ")
print ()
print ("Range:", (max(scores)-min(scores)))
print ()

while True:
    curve = input("Would you like to curve the exam? 'y' or 'n': ")
    if curve == "y":
        while True:
            x = float(input("Enter a desired mean (i.e. 75.0 to raise the mean score to 75.0): "))
            if x < (sum(scores)/len(scores)):
                print ("Invalid curve. Try again.")
            else:
                # create a new file
                newfile = open(filename+"_grades.txt", "w")
                # find curve points
                curvediff = x - (sum(scores)/len(scores))

                for m in range(0, len(students)):
                    n = students[m]
                    s = str(scores[m]) # convert integer to string
                    r = int(scores[m]+curvediff)+1 # round up
                    p = str(r)

                    newfile.write (n)
                    newfile.write (",")
                    newfile.write (s)
                    newfile.write (",")
                    newfile.write (p)
                    newfile.write ("\n")

                newfile.close()
                print ("Done! Check your grade file")
                break
        break
    elif curve == "n":

        newfile = open(filename+"_grades.txt", "w")

        for m in range(0, len(students)):
            n = students[m]
            p = str(scores[m])

            newfile.write (n)
            newfile.write (",")
            newfile.write (p)
            newfile.write ("\n")

        newfile.close()
        print ("Done!")
        break
    else:
        print ("Invalid option. Try again.")

