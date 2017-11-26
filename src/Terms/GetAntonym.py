from gensim.models.keyedvectors import KeyedVectors

from src.Utils import FileUtils
from src.Utils import Path

File_Path = "/Users/zlsun/IdeaProjects/Information-Retrieval/res/stem topics.txt"
Model_Path = Path.Data_Path + '/model/wiki.en.text.model'

model = KeyedVectors.load(Model_Path)
topic_query = FileUtils.openfile(File_Path)

for query in topic_query:
    q_list = query.split()

    for q in q_list:
        try:
            res = model.most_similar(positive=["good", q], negative=["bad"], topn=1)
            for item in res:
                print(item[0] + "," + str(item[1]))
                with open("AnOutput.txt", "a") as text_file:
                    text_file.write(item[0] + " " + str(item[1]) + "\r\n")
        except KeyError as e:
            pass
