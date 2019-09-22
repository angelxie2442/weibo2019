import jieba
import jieba.posseg as pseg
import jieba.analyse as ans

import csv

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation



import pyLDAvis
import pyLDAvis.gensim
import pyLDAvis.sklearn


##矫正
jieba.suggest_freq('5月', True)
jieba.suggest_freq('老男人', True)
jieba.suggest_freq('什么鬼', True)
jieba.suggest_freq('文化自信', True)
jieba.suggest_freq('跌了', True)
jieba.suggest_freq('特朗普', True)
jieba.suggest_freq('川普', True)


##extract content column from spreadsheet
content_list = []
with open('TrTwAllMay06th.csv') as content:
   reader=csv.reader(content,delimiter=',')
   for row in reader:
       content_list.append(row[3])
##remove title of the column
content_list.remove('content')



##tokenization (jieba)
for i in range(len(content_list)):
    document_cut = jieba.cut(content_list[i])
    result = '/'.join(document_cut)
    content_list[i]=result


##import stopword txt
sw_path = "stop_words.txt"
sw_dic = open(sw_path, 'rb')
sw_content = sw_dic.read()
#convert txt to stopwords list
sw_list = sw_content.splitlines()
sw_dic.close()



##vectorize
corpus = content_list
cntVector = CountVectorizer(stop_words=sw_list)
##term frequency-inverse document frequency
cntTf = cntVector.fit_transform(corpus)
##to access words bag:
word_bag= cntVector.get_feature_names()



lda = LatentDirichletAllocation(n_components=10,doc_topic_prior=0.001,topic_word_prior=0.8,learning_offset=50.,random_state=0)
####docres: topic/doc distribution
docres = lda.fit_transform(cntTf)




for topic_id,topic in enumerate(lda.components_):
    print(topic_id)
    word_ordered_array=[]
    ### argsort sort the word(indices) in ascending order
    ###only takes the top 30 words
    for i in range(30):
        word_ordered_array.append(word_bag[topic.argsort()[len(word_bag)-i-1]])
    print (">>>".join(word_ordered_array) )



####visualization
data=pyLDAvis.sklearn.prepare(lda, cntTf, cntVector)
pyLDAvis.displace(data)
#在notebook的output cell中显示
pyLDAvis.show(data)





