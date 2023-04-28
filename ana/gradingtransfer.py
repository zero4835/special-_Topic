import math

#Declare three sentiment variables
grading =['p0', 'p1', 'p2']

#init
for i in grading:
    locals()[i]=0.0
    
#transfer
def gradingTransfer(level, grade):
    global p0, p1, p2
    
    
    p0=p1=p2=0.0
    
    #counting r(x)
    r=(2 * (grade - 1)) / (level - 1)
    floor_r = math.floor(r)
    #print("r=%f, floor_r=%f\n" % (r, floor_r))
    
    #first condition
    var_name=f"p{floor_r}"
    p = 1 - r + floor_r
    globals()[var_name] = format(p, '.3f')

    #second condition
    var_name=f"p{floor_r+1}"
    p = r - floor_r
    globals()[var_name] = format(p, '.3f')
    
    #third condition
    if p0 != 0.0 and p1 != 0.0:
        p2 = 0.0
    elif p1 != 0.0 and p2 != 0.0:
        p0 = 0.0
    else:
        p1 = 0.0

    return {'neg': p0, 'neu': p1, 'pos': p2}   

#determin the grading sentiment
def determineSentiment(dic):
    max=-1.0
    max_term=""
    
    for i in dic:
        if float(dic[i]) > float(max):
            max_term=i
            max=dic[i]
    
    if max_term == 'neg':
        print("The sentiment is neg!")
    elif max_term == 'neu':
        print("The sentiment is neu!")
    else:
        print("The sentiment is pos!")
    
    #print("\n")
    return [max_term, max]
    

#S0 = neg S1 = neu S2 = pos
print("   S0 = neg       S1 = neu   S2 = pos\n")
print("0/10\n", gradingTransfer(10, 0))
print("\n5/10\n",gradingTransfer(10, 5)) 
print("\n6/7\n",gradingTransfer(7, 6)) 
print("\n3/5\n",gradingTransfer(5, 3)) 
print("\n60/100\n",gradingTransfer(100, 60)) 
print("\n8/9\n",gradingTransfer(9, 8)) 



dic=gradingTransfer(10, 0)
determineSentiment(dic)

dic=gradingTransfer(10, 5)
determineSentiment(dic)

dic=gradingTransfer(7, 6)
determineSentiment(dic)

dic=gradingTransfer(5, 3)
determineSentiment(dic)

dic=gradingTransfer(100, 60)
determineSentiment(dic)

dic=gradingTransfer(9, 8)
determineSentiment(dic)