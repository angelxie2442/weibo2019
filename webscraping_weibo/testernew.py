from bs4 import BeautifulSoup
import copy
import csv

from partition import takecontent
from partition import takeacctype
from partition import takeaccname

from contenttime import checkDatetime
from contenttime import checkFullcontent
from contenttime import removeDuplicate

from accnametype import accNameList
from accnametype import accTypeList

from combochart import separtime
from combochart import separcontent
from combochart import updatechart

import xmnlp
from snownlp import SnowNLP
from thulacnlp import replacing
from thulacnlp import addscore
from thulacnlp import addfivecolnames


completechart=[] #global var, continue to be built on

filelist=['wb01.htm','wb02.htm','wb03.htm','wb04.htm','wb05.htm','wb06.htm','wb07.htm','wb08.htm','wb09.htm','wb10.htm',
          'wb11.htm','wb12.htm','wb13.htm','wb14.htm','wb15.htm','wb16.htm','wb17.htm','wb18.htm','wb19.htm','wb20.htm']

       ##   'wb21.htm','wb22.htm','wb23.htm','wb24.htm','wb25.htm','wb26.htm','wb27.htm','wb28.htm','wb29.htm','wb30.htm',
       ##'wb31.htm','wb32.htm','wb33.htm','wb34.htm','wb35.htm','wb36.htm','wb37.htm','wb38.htm','wb39.htm','wb40.htm',
       ##'wb41.htm','wb42.htm','wb43.htm','wb44.htm','wb45.htm','wb46.htm','wb47.htm','wb48.htm','wb49.htm','wb50.htm']



for i in range(20):
    print(filelist[i])
    raw_html = open(filelist[i]).read()

    x=takecontent(raw_html)
    y=takeacctype(raw_html)
    z=takeaccname(raw_html)

    x1=removeDuplicate(x)
    typels=accTypeList(y)
    namels=accNameList(z)
    timels=separtime(x1)
    contentls=separcontent(x1)

    completechart=updatechart(completechart,timels,namels,typels,contentls)


##### NLP Test



#Cuz 中文分词不能recognize专有名词 所以换成english这样不影响情感分析还improve关键词分析准确性
#Also delete some unecessary stuffs (\n,blank,L...)
completechart1=replacing(completechart)


#chartwithscores
fivecolumnchart=addscore(completechart1)

print(len(fivecolumnchart))

#add titles to each of the five columns
chartfivetitle=addfivecolnames(fivecolumnchart)

print(len(chartfivetitle))
#chart with keywords
#sixcolumnchart=addkeywords(fivecolumnchart)

#sentiment score grouped by acctype


#sort by date per month and create a frequency table(later csv to be analyzed by R)


# sort by date per month and create a graph showing the sentiment changes （by R）




#write the data into a csv file
#def writechart(finalchart,csvfilename):

with open('TrumpJun2016.csv', "w", newline='') as my_csv:
    csvWriter = csv.writer(my_csv, delimiter=',')
    csvWriter.writerows(chartfivetitle)

    #return 1



