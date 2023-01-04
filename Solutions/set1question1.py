def converMarks(d):
    for students in d.keys():
        for marks in d[students].keys():
            m = d[students][marks]
            if m>=91 and m<=100:
                d[students][marks] = 'A'
            elif m>=81 and m<=90:
                d[students][marks] = 'B'
            elif m>=71 and m<=80:
                d[students][marks] = 'C'
            elif m>=61 and m<=70:
                d[students][marks] = 'D'
            elif m>=51 and m<=60:
                d[students][marks] = 'E+'
            elif m>=41 and m<=50:
                d[students][marks] = 'E'
            elif m>=0 and m<=40:
                d[students][marks] = 'F'
    return(d)

name = input().split()

d = {}
for i in name:
    d[i] = {}
    subjects = input().split()
    marks = input().split()
    for j in range(len(subjects)):
        d[i][subjects[j]] = int(marks[j])

print(converMarks(d))