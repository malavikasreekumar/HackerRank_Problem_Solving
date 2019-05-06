
def gradingStudents(grades):

    newgrade=[]
    for i in range(len(grades)):
        if grades[i] > 40 and grades[i] <=100:
            if ((((grades[i]//5)+1)*5)-grades[i]< 3 ):
                newgrade.append(((grades[i]//5)+1)*5)
            else:
                newgrade.append(grades[i])
        else:
            if grades[i]>=38 and grades[i] < 40:
                newgrade.append(40)
            else:
                newgrade.append(grades[i])
    return newgrade
    
