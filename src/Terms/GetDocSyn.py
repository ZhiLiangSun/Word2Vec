from gensim import models

from src.Utils import FileUtils
from src.Utils import Path
from src.Utils import Topic

import os

File_Path = "/Users/zlsun/IdeaProjects/Information-Retrieval/res/docTerm/"
W_File_Path = "C:\\Users\\Lab714\\Desktop\\Information-Retrieval\\res\\docTerm\\"
Model_Path = os.path.join(Path.Data_Path + os.sep, 'model', 'wiki2.en.text.model')
model = models.Word2Vec.load(Model_Path)

for topic in Topic.topics_100:
    topic_term_list = FileUtils.openfile(File_Path + str(topic) + "r")
    des = os.path.join(Path.Data_Path + os.sep, "synTerm" + os.sep, "docR" + os.sep, str(topic))
    for term_list in topic_term_list:
        term = term_list.split()
        for t in term:
            with open(des, "a", encoding='utf8', newline='') as text_file:
                text_file.write(t + '\r\n')
            try:
                res = model.most_similar(t, topn=20)
                for item in res:
                    print(item[0] + "," + str(item[1]))
                    with open(des, "a", encoding='utf8', newline='') as text_file:
                        text_file.write(item[0] + " " + str(item[1]) + '\r\n')
            except KeyError as e:
                pass
