from gensim.models.keyedvectors import KeyedVectors
import FileUtils

file_path = "/Users/zlsun/IdeaProjects/Information-Retrieval/res/stem topics.txt"
model_path = "/Users/zlsun/PycharmProjects/Word2vec/wiki.en.word2vec.model"


model = KeyedVectors.load(model_path)
topic_query = FileUtils.openfile(file_path)

for query in topic_query:
    q_list = query.split()

    for q in q_list:
        try:
            res = model.most_similar(q, topn=1)
            for item in res:
                print(item[0] + "," + str(item[1]))
        except KeyError as e:
            pass



