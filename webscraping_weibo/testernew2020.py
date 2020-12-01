from bs4 import BeautifulSoup
import copy
import csv
from partition import takecontent
from partition import takeacctype
from partition import taketime
from partition import takeaccname
from combochart import updatechart
import xmnlp
from snownlp import SnowNLP
from combinednlp import replacing
from combinednlp import addscore
from combinednlp import addfivecolnames

completechart=[]
num_htmFiles=78
filelist=["wb"+str(a+1)+".htm" for a in range(num_htmFiles)]
for i in range(78):
    print(filelist[i])
    raw_html = open(filelist[i], encoding="utf8").read()
    contentls=takecontent(raw_html)
    typels=takeacctype(raw_html)
    namels=takeaccname(raw_html)
    timels=taketime(raw_html)
    completechart=updatechart(completechart,timels,namels,typels,contentls)

completechart1=replacing(completechart)

#add sentiment scores to chart
fivecolumnchart=addscore(completechart1)
#add titles to each of the five columns
chartfivetitle=addfivecolnames(fivecolumnchart)
with open('../weibo2020.csv', "w", newline='', encoding="utf8") as my_csv:
    csvWriter = csv.writer(my_csv, delimiter=',')
    csvWriter.writerows(chartfivetitle)
