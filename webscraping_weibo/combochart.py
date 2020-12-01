import copy
#combine all the columns into final chart

#building the 4-column array
def updatechart(finalchart,timels,namels,typels,contentls):
    if(len(typels)<len(namels)):
        typels.append("微博未知")
    finalchart1=copy.deepcopy(finalchart)
    a=len(finalchart)#save the previous length
    for i in range(len(timels)):
        print(i)
        print(namels[i])
        finalchart1.append([])
        finalchart1[a+i].append(timels[i])
        finalchart1[a+i].append(namels[i])
        finalchart1[a+i].append(typels[i])
        finalchart1[a+i].append(contentls[i])
    return finalchart1



