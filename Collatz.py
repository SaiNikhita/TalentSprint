def next_num(num):
    if num%2==0:
        return int(num/2)
    else:
        return 3*num+1

def computeSeries(num,series):
    series.append(num)
    if num==1:
        return series
    else:
        num=next_num(num)
        series=computeSeries(num,series)
        return series
num=7
series=[]
print(computeSeries(num,series))
