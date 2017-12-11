from gensim.models.keyedvectors import KeyedVectors
from gensim import models

from src.Utils import FileUtils
from src.Utils import Path

import os

File_Path = "/Users/zlsun/IdeaProjects/Information-Retrieval/res/TopicSet/unstem topics.txt"
W_File_Path = "C:\\Users\\Lab714\\Desktop\\Information-Retrieval\\res\\TopicSet\\unstem topics.txt"
Model_Path = os.path.join(Path.Data_Path + os.sep, 'model', 'wiki.en.text.model')

model = models.Word2Vec.load(Model_Path)
topic_query = FileUtils.openfile(File_Path)

count = 0

for query in topic_query:
    q_list = query.split()

    for q in q_list:
        try:
            res = model.most_similar(q, topn=3)
            for item in res:
                print(item[0] + "," + str(item[1]))
                with open("SyOutput.txt", "a", encoding='utf8', newline='') as text_file:
                    text_file.write(item[0] + " " + str(item[1]) + '\r\n')
        except KeyError as e:
            count = count + 1
            pass

print(count)
