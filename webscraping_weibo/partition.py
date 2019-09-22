from bs4 import BeautifulSoup
#this file will take out all the important stuffs(datetime,content,accname,&acctype)
#convert html format into lists of strings

# delete all the parts that come after <!--/微博card--> (微博排行榜)
# because we want to keep the part up to the second time 微博card shows (not the first time!!!)
def editraw(raw):

    c = 0
    while raw[c:c + 6] != '微博card':
        c = c + 1
    while raw[c + 7:c + 13] != '微博card':
        c = c + 1
    raw1 = raw[0:c - 1]

    return raw1

# take out the post content parts
def takecontent(raw):

    raw1=editraw(raw)
    soup= BeautifulSoup(raw1, 'html.parser')
    posts=[]
    for pa in soup.select('p'):
        posts.append(pa.text)
    return posts

# two lists are kept in the function to keep track of 普通用户
def takeacctype(raw):

    raw1=editraw(raw)
    soup = BeautifulSoup(raw1,'html.parser')
    r1 = soup.select("div a")
    r3=[]#for acctype
    r4=[]#for accname
    for q in range(len(r1)):
        r2 = str(r1[q])
        for w in range(len(r2)):
            if(r2[w:w+9]=="title=\"微博"):
                r3.append(r2)
            if (r2[w:w + 9] == 'nick-name'):
                r4.append(r2)
            #if the length is more than 1 step behind, that shows the title line does not exist->普通用户
            if (len(r3) < len(r4)-1):
                r3.append("title=\"微博普通")

    return r3

# two lists are kept in the function to keep track of 普通用户
def takeaccname(raw):

    raw1=editraw(raw)
    soup = BeautifulSoup(raw1,'html.parser')
    r1 = soup.select("div a")
    r3=[]#for acctype
    r4=[]#for accname
    for q in range(len(r1)):
        r2 = str(r1[q])
        for w in range(len(r2)):
            if(r2[w:w+9]=="title=\"微博"):
                r3.append(r2)
            if (r2[w:w + 9] == 'nick-name'):
                r4.append(r2)
            #if the length is more than 1 step behind, that shows the title line does not exist->普通用户
            if (len(r3) < len(r4)-1):
                r3.append("title=\"微博普通")

    return r4



