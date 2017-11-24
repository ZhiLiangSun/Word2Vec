# Word2Vec


Python implementation of Word2Vec

Package : Gensim 

Data Set : Wikipedia 

利用Wikipedia英文資料集訓練Word2Vec模型

---

#### Wikipedia Pre-Processing 

$ python3 W2V_wiki_Process.py wikiData.xml.bz2 wiki.en.text

#### Word2Vec model tranning

$ python3 W2V_tranning.py dir wiki.en.text.model wiki.en.text.vector

#### Word2Vec model testing

$ python3 W2V_demo.py wiki.en.word2vec.model
