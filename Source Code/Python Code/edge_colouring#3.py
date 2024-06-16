#edge colouring algorithm for subject with course IDs
import csv
def getdata():
    file="main.csv"
    data=[]
    with open(file,"r") as csvfile:
        reader=csv.reader(csvfile)
        for row in reader:
            data.append(row)
        H=[]
        L=[]
        teach=[]
        for i in range(1,len(data)):
            #templ=[]
            L.append(data[i][1])
            if i%2==0:
                teach.append([data[i][2]+"3 B "+str(data[i][5]),data[i][3]+" 5 B "+str(data[i][6]),data[i][4]+" 7 B "+str(data[i][7])])
            else:
                teach.append([data[i][2]+" 3 A "+str(data[i][5]),data[i][3]+" 5 A "+str(data[i][6]),data[i][4]+" 7 A "+str(data[i][7])])
        distinct_class=[]
        for i in teach:
            for j in i:
                if ((j not in distinct_class) and ('NULL' not in j)):
                    distinct_class.append(j)
        for i in range(0,len(L)):
            k=[]
            c=0
            for j in range(0,len(distinct_class)):
                if distinct_class[j] in teach[i]:
                    k.append(int(teach[i][teach[i].index(distinct_class[j])][-1]))
                else:
                    k.append(0)
                c+=1
            H.append(k)
    return H,L,teach,distinct_class
def Colouring(H,teach1):
    max_degree=sum(H[0])#initializing a random possible value for the maximum degree
    max_lec=0#initializing a random possible value for the lecurer with the maximum degree
    #to obtain maximum degree of the bipartite graph
    index=0
    for i in H:
        if sum(i)>max_degree:
            max_degree=sum(i)
            max_lec=index
        index+=1
    #max_degree represents the chromatic number according to Konig's Theorem
    Colours=[]
    for n in range(1,max_degree+1):
        Colours.append(n)
    Edges=[]
    k=0#represents each subject - dimension of each small array
    temp=0
    for j in H[max_lec]:
        if j!=0:
            for hour in range(1,j+1):
                Edges.append(["L"+str(max_lec+1),teach1[max_lec][k],hour,Colours[temp]])
                temp+=1
            k+=1
    return max_lec,Edges,Colours
def check(temp,index,k,Edges,Colours1,teach1,arr1):
    for x in Edges:
        if ((x[0]=="L"+str(index+1)) or (x[1]==teach1[index][k])):
            n=x[3]
            arr1.append(n)
    if Colours1[temp] not in arr1:
        return Colours1[temp]
    else:
        return check((temp+1)%len(Colours1),index,k,Edges,Colours1,teach1,arr1)    
def Continue(max_lec,Edges,H,teach1,Colours1):
    index=0
    for i in H:
        k=0
        temp=0
        if i!=H[max_lec]:
            for j in i:
                if j!=0:
                    for hour in range(1,j+1):
                        arr=[]
                        res=check(temp,index,k,Edges,Colours1,teach1,arr)
                        Edges.append(["L"+str(index+1),teach1[index][k],hour,res])
                        temp+=1
                    k+=1
        index+=1
    return Edges
#main program
#Array of courses taught by the Lith Lecturer stored in the (i-1)th position
H_main,L_main,teach_main,x=getdata()
print(H_main)
print("\n\n")
a,L,b=Colouring(H_main,teach_main)
print(a)
print("\n\n")
print(b)
print("\n\n")
print(Continue(a,L_main,H_main,teach_main,b))
