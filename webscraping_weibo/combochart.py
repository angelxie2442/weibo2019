import copy
#######combine all the columns into final chart#######

#divide the time and content
def separtime(originallist):


    timelist=[]
    for a in range(len(originallist)):
        print(a)
        print(originallist[a])
        if a%2==1:
            c=0

            while ((originallist[a])[c]=='月' and (originallist[a])[c+3]=='日')==False:

                c=c+1
                #if(c==len(originallist[a])):
                  #timelist.append()
            # insert into the list
            timelist.append((originallist[a])[c-2:c+15])
    return timelist

def separcontent(originallist):
    contentlist=[]
    for a in range(len(originallist)):
        if a%2==0:
            contentlist.append(originallist[a])
    return contentlist


#building the 4-column array
def updatechart(finalchart,timels,namels,typels,contentls):



    if(len(typels)<len(namels)):
        typels.append("微博未知")


    #for lll in range(len(timels)):


    finalchart1=copy.deepcopy(finalchart)
    a=len(finalchart)#dont for get to save the previous length
    #so that it will start adding elements to the newly created lists
    for i in range(len(timels)):
        print(i)
        print(namels[i])
        print(timels[i])
        finalchart1.append([])
        finalchart1[a+i].append(timels[i])
        finalchart1[a+i].append(namels[i])
        finalchart1[a+i].append(typels[i])
        finalchart1[a+i].append(contentls[i])
    return finalchart1



