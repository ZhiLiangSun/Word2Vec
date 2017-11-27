from gensim.models import word2vec
from gensim.models.keyedvectors import KeyedVectors
from gensim import models

import logging
import sys
import os

from src.Utils import Path


def main():
    inp = sys.argv[1]
    Model_Path = os.path.join(Path.Data_Path + os.sep, 'model' + inp)

    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    # model = KeyedVectors.load(Model_Path)
    model = models.Word2Vec.load(Model_Path)

    # for Google Pre-trained word and phrase vectors
    # model = models.KeyedVectors.load_word2vec_format(Model_Path, binary=True)

    print("提供 3 種測試模式\n")
    print("輸入一個詞，則去尋找前一百個該詞的相似詞")
    print("輸入兩個詞，則去計算兩個詞的餘弦相似度")
    print("輸入三個詞，進行類比推理")

    while True:
        try:
            query = input()
            q_list = query.split()

            if len(q_list) == 1:
                print("相似詞排序")
                res = model.most_similar(q_list[0], topn=10)

                for item in res:
                    print(item[0] + "," + str(item[1]))

            elif len(q_list) == 2:
                print("計算 Cosine 相似度")
                res = model.similarity(q_list[0], q_list[1])
                print(res)
            else:
                print("%s之於%s，如%s之於" % (q_list[0], q_list[1], q_list[2]))
                res = model.most_similar(positive=[q_list[1], q_list[2]], negative=[q_list[0]], topn=5)
                for item in res:
                    print(item[0] + "," + str(item[1]))
            print("----------------------------")
        except Exception as e:
            print(repr(e))


if __name__ == "__main__":
    main()
