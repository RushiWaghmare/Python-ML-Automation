
def filterX(Task,Elements):
    result= []
    for no in Elements:
        if(Task(no)== True):
            result.append(no)
    return result

def mapX(Task,Elements):
    result=[]
    for no in Elements:
        ret=Task(no)
        result.append(ret)
    return result

def reduceX(Task,Elements):
    sum=0
    for no in Elements:
        sum=Task(sum,no) # it will call add funtion
    return sum


cheakeven=lambda n : (n%2==0)

Increase =lambda n:  n+1

Add =lambda a,b : a+b