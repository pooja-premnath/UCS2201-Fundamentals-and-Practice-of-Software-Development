import csv
import random
import json

d={'L11':['UCS1511', 'UCS1511','UCS1511','UCS1501','UCS1524','UCS1501','UCS1524','UCS1501','UCS1524'],
  'L13':['UCS1502', 'UCS1711','UCS1711','UCS1711','UCS1526','UCS1502','UCS1526'	,'UCS1502','UCS1526'],
  'L15':['UCS1701','UCS1503','UCS1512','UCS1512','UCS1512','UCS1701','UCS1503','UCS1701','UCS1503'],
  'L17':['UCS1504','UCS1712','UCS1712','UCS1712','UCS1504','UCS1504'],
  'L5':['UCS2301','UCS1505','UCS2301','UCS1505','UCS2311', 'UCS2311','UCS2311','UCS1505','UCS2301'],
'L7':['UCS2302'	,'UCS2302', 'UCS1723','UCS1723','UCS2302', 'UCS1723','UCS2312','UCS2312','UCS2312'],
'L9':['UCS1704'	,'UCS1704', 'UCS1704','UCS2303'	,'UCS2303','UCS2313','UCS2313','UCS2313','UCS2303'],
'L1':['UMA2377','UMA2377','UMA2377','UMA2377'],
'L19':[	'UCS1703','UCS1722' ,'UCS1722','UCS1703','UCS1703','UCS1722'],
'L21':[	'UCS1729',  'UCS1729','UCS1702','UCS1729','UCS1702','UCS1702'],
'L3':['UHS2351'	,'UHS2351', 'UHS2351']
}


stuck=0
def theory_allot(x):
    occur=1
    space=1
    teacher=1
    global count,alloted,s3,s5,s7
    if x[3]=='3':
        year=s3
        set1=s5
        set2=s7
    elif x[3]=='5':
        year=s5
        set1=s3
        set2=s7
    else:
        year=s7
        set1=s3
        set2=s5

    for i in range(len(set1)):
        day=set1[i]
        for j in range(len(day)):
            if type(day[j])==tuple:

                if day[j][1]==x[2]:

                    if set2[i][j]==0 and year[i][j]==0:
                        occur=1
                        space=1
                        teacher=1
                        occur=occurrence_check(x[0],year[i])

                        if x[3]=='3':                      #check if the course occurs once a day
                            space=thirdsem_check(day)

                        if space==1 and occur==1:
                            count+=1
                            year[i][j]=(x[0],x[2],x[1])
                            alloted.append((x[0],x[2],x[1]))

                            return


                    elif type(set2[i][j])==tuple and set2[i][j][1]==x[2] and year[i][j]==0: #when another course is occupied
                        occur=1
                        space=1
                        teacher=1
                        occur=occurrence_check(x[0],year[i]) #check if the course occurs once a day

                        teacher=teacher_check(x[0],set2[i][j][0],set1[i][j][0])
                        if x[3]=='3':
                            space=thirdsem_check(day)

                        if space==1 and occur==1 and teacher==1:
                            count+=1
                            year[i][j]=(x[0],x[2],x[1])
                            alloted.append((x[0],x[2],x[1]))
                            return


    occur=1
    space=1
    teacher=1
    for i in range(len(set2)):
        day=set2[i]
        for j in range(len(day)):

            if type(day[j])==tuple:
                if day[j][1]==x[2]:
                    if set1[i][j]==0 and year[i][j]==0:
                        occur=1
                        space=1
                        teacher=1
                        occur=occurrence_check(x[0],year[i])

                        if x[3]=='3':                      #check if the course occurs once a day
                            space=thirdsem_check(year[i])

                        if space==1 and occur==1 :
                            count+=1
                            year[i][j]=(x[0],x[2],x[1])
                            alloted.append((x[0],x[2],x[1]))
                            return


                    elif type(set1[i][j])==tuple and set1[i][j][1]==x[2] and year[i][j]==0: #when another course is occupied
                        occur=1
                        space=1
                        teacher=1
                        occur=occurrence_check(x[0],year[i]) #check if the course occurs once a day

                        teacher=teacher_check(x[0],set2[i][j][0],set1[i][j][0])
                        if x[3]=='3':
                            space=thirdsem_check(year[i])

                        if space==1 and occur==1 and teacher==1:
                            count+=1
                            year[i][j]=(x[0],x[2],x[1])
                            alloted.append((x[0],x[2],x[1]))
                            return
    #once color id fails
    occur=1
    space=1
    if x[2]=='1':
        for i in range(len(year)):
            for j in range(len(year[i])):
                if year[i][j]==0:
                    if set1[i][j]==0 and set2[i][j]==0:
                        occur=1
                        space=1
                        teacher=1
                        occur=occurrence_check(x[0],year[i]) #check if the course occurs once a day
                        if x[3]=='3':
                            space=thirdsem_check(year[i])

                        if space==1 and occur==1:
                            count+=1
                            year[i][j]=(x[0],x[2],x[1])
                            alloted.append((x[0],x[2],x[1]))
                            return

    elif int(x[2])>1:
        for i in range(len(year)):
            for j in range(len(year[i])):
                if year[i][j]==0:       #check for any empty position in the given semester
                    if type(set1[i][j])==tuple and type(set2[i][j])==tuple:     #courses present in both other sems
                        if int(set1[i][j][1])<int(x[2]) and int(set2[i][j][1])<int(x[2]):
                            occur=1
                            space=1
                            teacher=1
                            occur=occurrence_check(x[0],year[i]) #check if the course occurs once a day
                            teacher=teacher_check(x[0],set2[i][j][0],set1[i][j][0]) #teacher-conflict check
                            if x[3]=='3':
                                space=thirdsem_check(year[i])

                            if space==1 and occur==1 and teacher==1:
                                count+=1
                                year[i][j]=(x[0],x[2],x[1])
                                alloted.append((x[0],x[2],x[1]))
                                return

                    if type(set1[i][j])==tuple and type(set2[i][j])==int: #one side has a course
                        if int(set1[i][j][1])<int(x[2]):
                            occur=1
                            space=1
                            teacher=1
                            occur=occurrence_check(x[0],year[i]) #check if the course occurs once a day
                            teacher=two_teacher_check(x[0],set1[i][j][0])
                            if x[3]=='3':
                                space=thirdsem_check(year[i])

                            if space==1 and occur==1 and teacher==1:
                                count+=1
                                year[i][j]=(x[0],x[2],x[1])
                                alloted.append((x[0],x[2],x[1]))
                                return

                    if type(set2[i][j])==tuple and type(set1[i][j])==int:
                        if int(set2[i][j][1])<int(x[2]):
                            occur=1
                            space=1
                            teacher=1
                            occur=occurrence_check(x[0],year[i]) #check if the course occurs once a day
                            teacher=two_teacher_check(x[0],set2[i][j][0])
                            if x[3]=='3':
                                space=thirdsem_check(year[i])

                            if space==1 and occur==1 and teacher==1:
                                count+=1
                                year[i][j]=(x[0],x[2],x[1])
                                alloted.append((x[0],x[2],x[1]))
                                return

                    if type(set1[i][j])==int and type(set2[i][j])==int:
                        occur=1
                        space=1
                        if x[3]=='3':
                                space=thirdsem_check(year[i])

                        if space==1 and occur==1:
                            count+=1
                            year[i][j]=(x[0],x[2],x[1])
                            alloted.append((x[0],x[2],x[1]))
                            return




def occurrence_check(sub,year):
    sub_counter=0
    for i in range(len(year)):
        if type(year[i])==tuple:
            if year[i][0]==sub:
                sub_counter+=1
    if sub_counter==0:
        return 1
    else:
        return 0


def thirdsem_check(day):
    if day.count(0)>1:
        return 1
    else:
        return 0

def teacher_check(sub1,sub2,sub3):
    global d
    sub_lst=[sub1,sub2,sub3]
    teacher_set=set()
    for i in range(3):
        for j in d:
            for k in range(len(d[j])):
                if d[j][k]==sub_lst[i]:
                    teacher_set.add(j)

    if len(teacher_set)==3:
        return 1
    else:
        return 0

def two_teacher_check(sub1,sub2):
    global d
    sub_lst=[sub1,sub2]
    teacher_set=set()
    for i in range(2):
        for j in d:
            for k in range(len(d[j])):
                if d[j][k]==sub_lst[i]:
                    teacher_set.add(j)

    if len(teacher_set)==2:
        return 1
    else:
        return 0


def lab_allot(y):
    global lab_pop,s3,s5,s7
    ind=0
    lst=[]
    attempt=0
    allot=False
    pos=[[0,1,2],[1,2,3],[3,4,5]]  #possible slots where labs can be scheduled
    if y[0][3]=='3':
        yr=3
        day=s3
    elif y[0][3]=='5':
        yr=5
        day=s5
    else:
        yr=7
        day=s7

    while allot==False:
        attempt+=1
        day_choice=0
        while day_choice==0:
            ind=random.choice([0,1,2,3,4])  #choosing a random, and checking if there is any other lab scheduled on the same day
            lst=day[ind]
            if lst.count(0)==6:
                day_choice=1
        place=random.choice(pos)
        c_id=0
        for i in range(3):
            lst[place[i]]=(y[i][0],y[i][2],y[i][1]) #allocate period to slots
        c_id=colorid_check(yr,lst,ind)      #checking the color ids, to avoid overlap
        if c_id==1:
            allot=True
            return 1

        if c_id!=1:
            for i in range(3):
                lst[place[i]]=0

        if attempt>20:
            return 0



def list_populate(lst):
    for i in range(5):
        lst.append([])
        for j in range(6):
            lst[i].append(0)


def colorid_check(yr,lst,ind):

    global s3,s5,s7
    if yr==3:           #determining which other years the current year must be checked with
        set1=s5[ind]
        set2=s7[ind]
    elif yr==5:
        set1=s3[ind]
        set2=s7[ind]
    else:
        set1=s3[ind]
        set2=s5[ind]
    counter=0
    for i in range(6):
        if lst[i]!=0:
            if (set1[i]==0 and set2[i]==0):             #different combinations of values and zeroes
                counter+=1
            elif type(set1[i])==tuple and type(set2[i])==tuple:
                if set1[i][1]==lst[i][1] and set2[i][1]==lst[i][1]:
                    counter+=1
            elif type(set1[i])==tuple and type(set2[i])==int:
                if set1[i][1]==lst[i][1]:
                    counter+=1
            elif type(set1[i])==int and type(set2[i])==tuple:
                if set2[i][1]==lst[i][1]:
                    counter+=1
            else:
                pass

    if counter==3:
        return 1
    else:
        return 0


def teacher_hours(sem,num):
    global hours, classes
    for i in range(len(sem)):
        for j in range(len(sem[i])):
            if type(sem[i][j])==tuple:
                teacher=sem[i][j][2]
                if teacher in hours:
                    hours[teacher]+=1
                else:
                    hours[teacher]=1

    for i in range(len(sem)):
        for j in range(len(sem[i])):
            if type(sem[i][j])==tuple:
                teacher=sem[i][j][2]
                if teacher in classes:
                    classes[teacher].append(['sem: '+str(num), 'day: '+ str(i),'period: '+str(j),'class: '+sem[i][j][0]])
                else:
                    classes[teacher]=[]
                    classes[teacher].append(['sem: '+str(num), 'day: '+ str(i),'period: '+str(j),'class: '+sem[i][j][0]])

def printing_b():
    return s3_tup,s5_tup,s7_tup,data3a,data5a,data7a,L1,L3,L5,L7,L9,L11,L13,L15,L17,L19,L21
#main
#opening the required CSV files for A section
courses=[]
course_counter=0
f2=open("trial.csv",'r',newline='')
readerobj2=list(csv.reader(f2))
for i in range(1,len(readerobj2)):
    courses.append(readerobj2[i])
labs=[courses[i:i+3] for i in range(0,21,3)]
theory=[]
f=open('theory_color.csv','r',newline='')
readerobj=list(csv.reader(f))
for i in range(1,len(readerobj)):
    theory.append(readerobj[i])

hours={}
classes={}
count=0
lab_pop=0


while count!=58:
    count=0
    alloted=[]
    s7=[]
    s5=[]
    s3=[]
    list_populate(s7)
    list_populate(s5)
    list_populate(s3)
    lab_count=0

    while lab_count<7:
        stat=lab_allot(labs[lab_count])
        if stat==1:
            lab_count+=1
        else:
            lab_count=0
            s7=[]
            s5=[]
            s3=[]
            list_populate(s7)
            list_populate(s5)
            list_populate(s3)

    else:
        print("Labs alloted successfully")


    for i in range(len(s3)):
        weekday=s3[i]
        if weekday.count(0)==6:
            weekday.insert(4,"Lunch")
        elif weekday[3]!=0 and weekday[4]!=0 and weekday[5]!=0:
            weekday.insert(3,"Lunch")
        else:
            weekday.insert(4,"Lunch")

    for i in range(len(s5)):
        weekday=s5[i]
        if weekday.count(0)==6:
            weekday.insert(4,"Lunch")
        elif weekday[3]!=0 and weekday[4]!=0 and weekday[5]!=0:
            weekday.insert(3,"Lunch")
        else:
            weekday.insert(4,"Lunch")

    for i in range(len(s7)):
        weekday=s7[i]
        if weekday.count(0)==6:
            weekday.insert(4,"Lunch")
        elif weekday[3]!=0 and weekday[4]!=0 and weekday[5]!=0:
            weekday.insert(3,"Lunch")
        else:
            weekday.insert(4,"Lunch")

    for i in theory:
        theory_allot(i)
    print("No of theory courses alloted:", count)
    '''print(s3)
    print(s5)
    print(s7)'''
    var=True

teacher_hours(s3,3)
teacher_hours(s5,5)
teacher_hours(s7,7)
'''print('Semester 3')
print(s3)
print()
print('Semester 5')
print(s5)
print()
print('Semester 7')
print(s7)'''
#printing_b()
print()
print(hours)
total=0
for i in hours:
    total+=hours[i]
print("Total no of hours",total)
print()
print("No of theory courses alloted:", count)
print(json.dumps(classes,indent=2))

sup=["SPORTS", "MENTOR", "PCD","LIBRARY"]


f3=open('allotment.csv','r',newline='')
readerobj3=list(csv.reader(f3))
data3a=[]
data5a=[]
data7a=[]
data3b=[]
data5b=[]
data7b=[]
for i in range(2,len(readerobj3)):

    if readerobj3[i][3]=='3':
        if int(readerobj3[i][4][1:])%2!=0:
            data3a.append((readerobj3[i][0],readerobj3[i][1],readerobj3[i][2],readerobj3[i][4]))
        else:
             data3b.append((readerobj3[i][0],readerobj3[i][1],readerobj3[i][2],readerobj3[i][4]))
    elif readerobj3[i][3]=='5':
        if int(readerobj3[i][4][1:])%2!=0:
            data5a.append((readerobj3[i][0],readerobj3[i][1],readerobj3[i][2],readerobj3[i][4]))
        else:
             data5b.append((readerobj3[i][0],readerobj3[i][1],readerobj3[i][2],readerobj3[i][4]))
    else:
        if int(readerobj3[i][4][1:])%2!=0:
            data7a.append((readerobj3[i][0],readerobj3[i][1],readerobj3[i][2],readerobj3[i][4]))
        else:
             data7b.append((readerobj3[i][0],readerobj3[i][1],readerobj3[i][2],readerobj3[i][4]))

data3a=tuple(data3a)
data3b=tuple(data3b)
data5a=tuple(data5a)
data5b=tuple(data5b)
data7a=tuple(data7a)
data7b=tuple(data7b)


L1=[[0 for j in range(7)] for i in range(5)]
L2=[[0 for j in range(7)] for i in range(5)]
L3=[[0 for j in range(7)] for i in range(5)]
L4=[[0 for j in range(7)] for i in range(5)]
L5=[[0 for j in range(7)] for i in range(5)]
L6=[[0 for j in range(7)] for i in range(5)]
L7=[[0 for j in range(7)] for i in range(5)]
L8=[[0 for j in range(7)] for i in range(5)]
L9=[[0 for j in range(7)] for i in range(5)]
L10=[[0 for j in range(7)] for i in range(5)]
L11=[[0 for j in range(7)] for i in range(5)]
L12=[[0 for j in range(7)] for i in range(5)]
L13=[[0 for j in range(7)] for i in range(5)]
L14=[[0 for j in range(7)] for i in range(5)]
L15=[[0 for j in range(7)] for i in range(5)]
L16=[[0 for j in range(7)] for i in range(5)]
L17=[[0 for j in range(7)] for i in range(5)]
L18=[[0 for j in range(7)] for i in range(5)]
L19=[[0 for j in range(7)] for i in range(5)]
L20=[[0 for j in range(7)] for i in range(5)]
L21=[[0 for j in range(7)] for i in range(5)]
L22=[[0 for j in range(7)] for i in range(5)]
L24=[[0 for j in range(7)] for i in range(5)]
L26=[[0 for j in range(7)] for i in range(5)]

'''for key in classes:
    lecturer=key
    lst=globals()['L'+str(lecturer[1:])]
    for j in range(len(classes[key])):
        #print(int(classes[key][j][1][5]))
        lst[int(classes[key][j][1][5])][int(classes[key][j][1][5])]=classes[key][j][3][7:]

    print(lst)
    print()'''

for key in classes:
    lecturer=key
    lst=globals()['L'+str(lecturer[1:])]
    for j in range(len(classes[key])):
        #print(key,int(classes[key][j][1][5]),(classes[key][j][2][8]))
        lst[int(classes[key][j][1][5])][int(classes[key][j][2][8])]=classes[key][j][3][7:]


    for k in range(len(lst)):
        lst[k]=tuple(lst[k])
    lst=tuple(lst)
    print()
    '''for q in range(len(lst)):
        for p in range(len(lst[q])):
            if lst[q][p]==0:
                lst[q][p]=''
    lst=tuple(lst)
    #print(lst)'''


'''print('data3a',data3a)
print('data3b',data3b)
print()
print('data5a',data5a)
print('data5b',data5b)
print()
print('data7a',data7a)
print('data7b',data7b)
print() '''


for i in range(len(s3)):
    for j in range(7):
        if type(s3[i][j])==tuple:
            s3[i][j]=s3[i][j][0]
        if s3[i][j]==0:
            s3[i][j]=random.choice(sup)
    s3[i]=tuple(s3[i])
s3_tup=tuple(s3)


for i in range(len(s5)):
    for j in range(7):
        if type(s5[i][j])==tuple:
            s5[i][j]=s5[i][j][0]
        if s5[i][j]==0:
            s5[i][j]=random.choice(sup)
    s5[i]=tuple(s5[i])
s5_tup=tuple(s5)


for i in range(len(s7)):
    for j in range(7):
        if type(s7[i][j])==tuple:
            s7[i][j]=s7[i][j][0]
        if s7[i][j]==0:
            s7[i][j]=random.choice(sup)
    s7[i]=tuple(s7[i])
s7_tup=tuple(s7)

'''print('s3_tup',s3_tup)
print()
print('s5_tup',s5_tup)
print()
print('s7_tup',s7_tup)'''


