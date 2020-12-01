import jieba
import jieba.posseg as pseg
import jieba.analyse as ans



import csv
import sklearn
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer


import pyLDAvis
import pyLDAvis.gensim
import pyLDAvis.sklearn




##extract content column from spreadsheet
content_list = []
with open('TrTwAllCompleteMay07080910th.csv') as content:
   reader=csv.reader(content,delimiter=',')
   for row in reader:
       content_list.append(row[3])
##remove title of the column
content_list.remove('content')


doc_length=[]
##tokenization (jieba)
for i in range(len(content_list)):
    document_cut = jieba.cut(content_list[i])
    result = '/'.join(document_cut)

    ##re-split the string to get doc.length
    split_list=result.split('/')
    doc_length.append(len(split_list))
    content_list[i]=result

print(len(doc_length))

##import stopword txt
sw_path = "stop_words.txt"
sw_dic = open(sw_path, 'rb')
sw_content = sw_dic.read().decode('utf-8')
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



lda = LatentDirichletAllocation(n_components=6,doc_topic_prior=0.01,topic_word_prior=5,learning_offset=50.,random_state=0)
####docres: topic/doc distribution
docres = lda.fit_transform(cntTf)

for a,b in enumerate(cntTf.vocabulary_):
    print(a)


for topic_id,topic in enumerate(lda.components_):
    word_ordered_array=[]
    ### argsort sort the word(indices) in ascending order
    ###only takes the top 30 words
    for i in range(30):
        word_ordered_array.append(word_bag[topic.argsort()[len(word_bag)-i-1]])
    print (">>>".join(word_ordered_array) )




###vocab
with open('lda_vocab.csv', "w") as my_csv:
    csvWriter = csv.writer(my_csv)
    my_csv.write('header')
    my_csv.write('\n')
    for line in word_bag:
        my_csv.write(line)
        my_csv.write('\n')

###term frequency
with open('lda_tf.csv', "w", newline='') as my_csv:
    csvWriter = csv.writer(my_csv, delimiter=',')
    csvWriter.writerows(cntTf)




####visualization
##data=pyLDAvis.sklearn.prepare(lda, cntTf, cntVector)
#pyLDAvis.displace(data)
#在notebook的output cell中显示
#pyLDAvis.show(data)





