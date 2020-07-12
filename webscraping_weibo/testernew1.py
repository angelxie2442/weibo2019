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
from combinednlp import replacing
from combinednlp import addscore
from combinednlp import addfivecolnames


completechart=[] #global var, continue to be built on
filelist1=['wb_svd1.htm','wb_svd2.htm','wb_svd3.htm']
filelist=['wb1.htm','wb2.htm','wb3.htm','wb4.htm','wb5.htm','wb6.htm','wb7.htm','wb8.htm','wb9.htm','wb10.htm',
          'wb11.htm','wb12.htm','wb13.htm','wb14.htm','wb15.htm','wb16.htm','wb17.htm','wb18.htm','wb19.htm','wb20.htm',
          'wb21.htm','wb22.htm','wb23.htm','wb24.htm','wb25.htm','wb26.htm','wb27.htm','wb28.htm','wb29.htm','wb30.htm',
          'wb31.htm','wb32.htm','wb33.htm','wb34.htm','wb35.htm','wb36.htm','wb37.htm','wb38.htm','wb39.htm','wb40.htm',
          'wb41.htm','wb42.htm','wb43.htm','wb44.htm','wb45.htm','wb46.htm','wb47.htm','wb48.htm','wb49.htm','wb50.htm',
          'wb51.htm','wb52.htm','wb53.htm','wb54.htm','wb55.htm','wb56.htm','wb57.htm','wb58.htm','wb59.htm','wb60.htm',
          'wb61.htm','wb62.htm','wb63.htm','wb64.htm','wb65.htm','wb66.htm','wb67.htm','wb68.htm','wb69.htm','wb70.htm',
          'wb71.htm','wb72.htm','wb73.htm','wb74.htm','wb75.htm','wb76.htm','wb77.htm','wb78.htm','wb79.htm','wb80.htm']

for i in range(2):
    print(filelist[i])
    raw_html = open(filelist[i], encoding="utf8").read()
    x=takecontent(raw_html)
    y=takeacctype(raw_html)
    z=takeaccname(raw_html)

    x1=removeDuplicate(x)
    typels=accTypeList(y)
    namels=accNameList(z)
    timels=separtime(x1)
    contentls=separcontent(x1)

    completechart=updatechart(completechart,timels,namels,typels,contentls)

#Rrr

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



#write the data into a csv file
#def writechart(finalchart,csvfilename):

with open('./randtest.csv', "w", newline='', encoding="utf8") as my_csv:
    csvWriter = csv.writer(my_csv, delimiter=',')
    csvWriter.writerows(chartfivetitle)



