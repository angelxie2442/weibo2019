import copy
import xmnlp
from snownlp import SnowNLP


# replace some words with english before using snownlp
def replacing(chartold):
    chart = copy.deepcopy(chartold)
    for index in range((len(chart))):
        unece = (chart[index][3]).find('L')
        if unece > 0:
            chart[index][3] = (chart[index][3])[0:unece]
        chart[index][0] = (chart[index][0]).replace("\n", "")
        chart[index][3] = (chart[index][3]).replace("\n", "")
        chart[index][3] = (chart[index][3]).replace("特朗普", "Trump")
        chart[index][3] = (chart[index][3]).replace("推特", "Twitter")
        chart[index][3] = (chart[index][3]).replace("收起全文d", "")
        chart[index][3] = (chart[index][3]).replace("O网页链接", "")
        chart[index][3] = (chart[index][3]).replace("秒拍视频", "")
        chart[index][3] = (chart[index][3]).replace("发推", "tweets")
        chart[index][3] = (chart[index][3]).replace("中兴", "ZTE")
        chart[index][3] = (chart[index][3]).replace("华为", "Huawei")
        chart[index][3] = (chart[index][3]).replace("【", "")
        chart[index][3] = (chart[index][3]).replace("】", "")
        chart[index][3] = (chart[index][3]).replace("...", ",")
        chart[index][3] = (chart[index][3]).replace("#", "")
        chart[index][3] = (chart[index][3]).replace("~", "")


    return chart


def addscore(chart):
    # add a column containing the sentiment score on the original 4-column chart
    chart1=copy.deepcopy(chart)
    for vvv in range(len(chart1)):
        if len((chart1[vvv])[3])==0:
            chart1[vvv].append("blank")
            chart1[vvv].append("blank")
            chart1[vvv].append("blank")
        else:
            x= (chart1[vvv])[3]
            s= SnowNLP(chart1[vvv][3])
            t1=xmnlp.sentiment(x)
            t2=s.sentiments
            t3=(t1+t2)/2
            chart1[vvv].append(t1)
            chart1[vvv].append(t2)
            chart1[vvv].append(t3)
    return chart1

def addfivecolnames(chart):
    chart1=[]
    chart1.append([])
    chart1[0].append('time')
    chart1[0].append('name')
    chart1[0].append('type')
    chart1[0].append('content')
    chart1[0].append('scoreXM')
    chart1[0].append('scoreSNOW')
    chart1[0].append('scoreAVG')
    for www in range(len(chart)):
        chart1.append([])
        chart1[www+1].append(chart[www][0])
        chart1[www+1].append(chart[www][1])
        chart1[www+1].append(chart[www][2])
        chart1[www+1].append(chart[www][3])
        chart1[www+1].append(chart[www][4])
        chart1[www+1].append(chart[www][5])
        chart1[www+1].append(chart[www][6])
    return chart1


