# Word2Vec


Python implementation of Word2Vec

Package : Gensim 

Data Set : Wikipedia 

利用Wikipedia英文資料集訓練Word2Vec模型

---

#### Wikipedia Pre-Processing 

$ python3 -m src.Model.W2V_wiki_Process wikiData.xml.bz2 wiki.en.text

#### Word2Vec model training

$ python3 -m src.Model.W2V_training wiki.en.text.model wiki.en.text.vector

#### Word2Vec model testing

$ python3 -m src.Model.W2V_demo wiki.en.text.model

#### Remove .DS_Store

$ find . -name '*.DS_Store' -type f -delete