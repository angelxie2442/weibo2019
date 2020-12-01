from bs4 import BeautifulSoup
#functions for extracting:content,datetime,acctype,accname
#delete all the parts that come after <!--/微博card--> (微博排行榜)
#keep the part till the second time as opposed to the first time '微博card' occurs
def editraw(raw):
    c = 0
    while raw[c:c + 6] != '微博card':
        c = c + 1
    while raw[c + 7:c + 13] != '微博card':
        c = c + 1
    raw1 = raw[0:c - 1]
    return raw1

# filter actual posts sections
def takecontent(raw):
    raw1=editraw(raw)
    soup= BeautifulSoup(raw1, 'html.parser')
    contentls=[]
    r1=soup.find_all(attrs={'node-type':['feed_list_content','feed_list_forwardContent','feed_list_content_full']})
    fC=False
    #number of posts= number of "feed_list_content" - number of "feed_list_forwardContent"
    s_prev=''
    for r1element in r1:
        if r1element.get('node-type')=="feed_list_forwardContent":
            fC=True
        elif r1element.get('node-type')=="feed_list_content" and fC==False:
            s_prev=r1element.get_text()
            contentls.append(r1element.get_text())
        elif r1element.get('node-type') =="feed_list_content" and fC==True:
            contentls.pop()
            contentls.append(s_prev+" 转发: "+(r1element.get_text()))
            s_prev=''
            fC=False
        elif r1element.get('node-type') =="feed_list_content_full":
            s_prev = r1element.textContent
            contentls.pop()
            contentls.append(r1element.get_text())
    return contentls

def taketime(raw):
    raw1=editraw(raw)
    soup= BeautifulSoup(raw1, 'html.parser')
    timels=[]
    r1 = soup.select('div p',{"class":"from"})
    #NOTE: number of posts= number of "feed_list_content" - number of "feed_list_forwardContent"
    for r1element in r1:
        if r1element.parent.get('class')==["content"] and r1element.get('class')==["from"]:
            timels.append(r1element.get_text())
    return timels

# two lists are kept in the function to keep track of 普通用户
def takeacctype(raw):
    raw1=editraw(raw)
    soup = BeautifulSoup(raw1,'html.parser')
    r1 = soup.select("div a")
    prev_is_name=False
    usernames=[]
    usertypes=[]
    for r1element in r1:
        if r1element.get('nick-name')is not None and r1element.parent.get('node-type') !="feed_list_forwardContent":
            #first check if last user has a type in the list (if not add "unknown" to usertype list)
            if (prev_is_name==True) and len(usernames)==len(usertypes)+1:
                usertypes.append("unknown")
            prev_is_name=True
            usernames.append(r1element.get('nick-name'))
        elif prev_is_name==True and r1element.get('title')is not None:
            titleoption= r1element.get('title')
            if titleoption=="微博官方认证" or titleoption=="微博会员" or titleoption=="微博个人认证" or titleoption=="微博达人":
                usertypes.append(titleoption)
                prev_is_name=False
    if prev_is_name==True:
        usertypes.append("unknown")
    return usertypes

# two lists are kept in the function to keep track of 普通用户
def takeaccname(raw):
    raw1=editraw(raw)
    soup = BeautifulSoup(raw1,'html.parser')
    r1 = soup.select("div a")
    prev_is_name=False
    usernames=[]
    usertypes=[]
    for r1element in r1:
        if r1element.get('nick-name')is not None and r1element.parent.get('node-type')!="feed_list_forwardContent":
            #first check if last user has a type in the list (if not add "unknown" to usertype list)
            if (prev_is_name==True) and len(usernames)==len(usertypes)+1:
                usertypes.append("unknown")
            prev_is_name=True
            usernames.append(r1element.get('nick-name'))
        elif prev_is_name==True and r1element.get('title')is not None:
            titleoption= r1element.get('title')
            if titleoption=="微博官方认证" or titleoption=="微博会员" or titleoption=="微博个人认证" or titleoption=="微博达人":
                usertypes.append(titleoption)
                prev_is_name=False
    if prev_is_name==True:
        usertypes.append("unknown")
    #temppp=soup.find_all('a',{"class":"name"})
    #temppp1=soup.find_all('a',{"target":"_blank"})
    return usernames



