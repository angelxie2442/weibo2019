import copy
from snownlp import SnowNLP
# replace some words with english before using snownlp
def replacing(chartold):
    chart = copy.deepcopy(chartold)
    for index in range((len(chart))):

        # this block of code is to get rid of "Lxxx" part at the end of the post content
        unece = (chart[index][3]).find('L')
        if unece > 0:
            chart[index][3] = (chart[index][3])[0:unece]

        chart[index][3] = (chart[index][3]).replace(" ", "")
        chart[index][0] = (chart[index][0]).replace(" ", "")
        chart[index][0] = (chart[index][0]).replace("\n", "")
        chart[index][3] = (chart[index][3]).replace("\n", "")
        chart[index][3] = (chart[index][3]).replace("霍华德·舒尔茨", "HowardSchultz")
        chart[index][3] = (chart[index][3]).replace("以色列", "Israel")
        chart[index][3] = (chart[index][3]).replace("耶路撒冷", "Jerusalem")
        chart[index][3] = (chart[index][3]).replace("特朗普", "trump")
        chart[index][3] = (chart[index][3]).replace("推特", "Twitter")
        chart[index][3] = (chart[index][3]).replace("星巴克", "Starbucks")
        chart[index][3] = (chart[index][3]).replace("默克尔", "Merkle")
        chart[index][3] = (chart[index][3]).replace("奥巴马", "Obama")
        chart[index][3] = (chart[index][3]).replace("收起全文d", "")
        chart[index][3] = (chart[index][3]).replace("O网页链接", "")
        chart[index][3] = (chart[index][3]).replace("秒拍视频", "")
        chart[index][3] = (chart[index][3]).replace("发推", "tweets")
        chart[index][3] = (chart[index][3]).replace("马杜罗", "Maduro")
        chart[index][3] = (chart[index][3]).replace("小金", "KimJong-un")
        chart[index][3] = (chart[index][3]).replace("金正恩", "KimJong-un")
        chart[index][3] = (chart[index][3]).replace("富士康", "Foxconn")
        chart[index][3] = (chart[index][3]).replace("的微博视频", "")
        chart[index][3] = (chart[index][3]).replace("亮了", "微妙")
        chart[index][3] = (chart[index][3]).replace("变脸", "翻脸")
        chart[index][3] = (chart[index][3]).replace("特金会", "峰会")
        chart[index][3] = (chart[index][3]).replace("中兴", "ZTE")
        chart[index][3] = (chart[index][3]).replace("华为", "Huawei")
        chart[index][3] = (chart[index][3]).replace("【", "")
        chart[index][3] = (chart[index][3]).replace("】", "")
        chart[index][3] = (chart[index][3]).replace("...", ",")
        chart[index][3] = (chart[index][3]).replace("#", "")
        chart[index][3] = (chart[index][3]).replace("~", "")
        chart[index][3] = (chart[index][3]).replace("迈克尔·贝内特", "MichaelBennet")
        chart[index][3] = (chart[index][3]).replace("赵小兰", "ElaineChao")
        chart[index][3] = (chart[index][3]).replace("拉黑", "block")
        chart[index][3] = (chart[index][3]).replace("全球变暖", "globalwarming")
        chart[index][3] = (chart[index][3]).replace("谷歌", "google")
        chart[index][3] = (chart[index][3]).replace("丹尼尔·拉格斯", "Daniel")
        chart[index][3] = (chart[index][3]).replace("马云", "JackMa")

    return chart


def addscore(chart):
    # add a column containing the sentiment score on the original 4-column chart
    chart1=copy.deepcopy(chart)
    for vvv in range(len(chart1)):
        if len((chart1[vvv])[3])==0:
            chart1[vvv].append("blank")
        else:
            s = SnowNLP(chart1[vvv][3])
             # s1 = s.summary(1)
             # s2=SnowNLP(s1[0])
            chart1[vvv].append(s.sentiments)
    return chart1

def addfivecolnames(chart):
    chart1=[]
    chart1.append([])
    chart1[0].append('time')
    chart1[0].append('name')
    chart1[0].append('type')
    chart1[0].append('content')
    chart1[0].append('score')


    for www in range(len(chart)):
        chart1.append([])
        chart1[www+1].append(chart[www][0])
        chart1[www+1].append(chart[www][1])
        chart1[www+1].append(chart[www][2])
        chart1[www+1].append(chart[www][3])
        chart1[www+1].append(chart[www][4])

    return chart1


