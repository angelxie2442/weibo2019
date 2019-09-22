
#futher cleaning/deleting

# test if it is the date/time
def checkDatetime(stringx):
    checkt = False
    j = stringx.find('月')
    k = stringx.find('日')
    q = stringx.find(':')

    if j > 0 and k > 0 and q > 0 and j + 3 == k and k + 4 == q:
        checkt = True
    return checkt

# test if it is the full content version-it can't be 展开全文 or the date/time
def checkFullcontent(stringx):

    chefull = True
    a = stringx.find('c')
    b = stringx.find('文')
    c = stringx.find('全')
    d = stringx.find('开')
    e = stringx.find('展')

    if a - 1 == b and b - 1 == c and c - 1 == d and d - 1 == e:
        chefull = False

    # eliminate the case where it is datetime
    elif checkDatetime(stringx)==True:
        chefull=False
    return chefull


# to delete the ones with (展开全文) so that the remaining is either date/time or full post content
def removeDuplicate(textlist):
    l=len(textlist)
    i=0
    while (i!=l):
        x=len(textlist[i])
        #if 1. not the full content format or 2. not an element indicating the time
        # 3. not main caption of the post (by testing it it is in between datetime and a main part of post)
        # then delete

        if (checkDatetime(textlist[i])==False) and (checkFullcontent(textlist[i])==False):
            #case1:not date/time or content(full version)
            del(textlist[i])
            l=l-1
            #case 2: not date/time, is full content but is not relevant main content (帖子点赞）
        elif i<l-1 and i>0 and checkDatetime(textlist[i])==False and checkDatetime(textlist[i-1])==False:
            #全文，无关，无关, 日期
            del (textlist[i])
            l = l - 1
        elif i<l-1 and ((textlist[i])[0:15]==(textlist[i+1])[0:15]):
            #directly checking if it is duplicates
            del (textlist[i])
            l = l - 1
        elif i<l-1 and i>0 and checkDatetime(textlist[i])==True and checkDatetime(textlist[i+1])==True:
            #转发帖子和自己帖子的时间两个连续的时间
            #删掉此次时间直到下一个不也是时间为止
            del (textlist[i])
            l = l - 1
        elif i<l and i>0 and checkDatetime(textlist[i-1])==True and checkDatetime(textlist[i])==True and (i%2==0):
            #上面只能检测之前的时间重复，这条能检测之后的时间重复，删去之后的那条（在双数号的那条）
            del(textlist[i])
            l = l - 1
        else:
           i=i+1
    return textlist