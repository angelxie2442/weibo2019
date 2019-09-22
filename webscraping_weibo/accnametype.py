from bs4 import BeautifulSoup


#extract names
def accNameList(parts):
    a=len(parts)
    nameList=[]
    for i in range(a):
        b=str(parts[i])
        for j in range(len(b)):
            if b[j:j+9]=="nick-name":
                nameList.append(b[j+11:j+16])

    return nameList

# extract account types
def accTypeList(parts):
    a=len(parts)
    typeList=[]
    for i in range(a):
        b=str(parts[i])
        for j in range(len(b)):
            if(b[j:j+9]=="title=\"微博"):
                typeList.append(b[j+7:j+11])

    return typeList