import logging
import os
import sys
import multiprocessing

from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
from gensim.models.word2vec import PathLineSentences

from src.Utils import Path

if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))

    # check and process input arguments
    if len(sys.argv) < 3:
        print(globals()['__doc__'] % locals())
        sys.exit(1)
    outp1, outp2 = sys.argv[1:3]

    DT_Path = os.path.join(Path.Data_Path + os.sep, 'parsed_data')
    Des_Path = os.path.join(Path.Data_Path + os.sep, 'model')

    outp1 = os.path.join(Des_Path + os.sep, outp1)
    outp2 = os.path.join(Des_Path + os.sep, outp2)

    sentences = PathLineSentences(DT_Path)
    model = Word2Vec(sentences, size=400, window=5, min_count=5,
                     workers=multiprocessing.cpu_count(), sg=0)
    model.save(outp1)
    word_vectors = model.wv
    # trim unneeded model memory = use(much) less RAM
    # model.init_sims(replace=True)
    word_vectors.save(outp2)

    # output2 at line 21
    # model.wv.save_word2vec_format(outp2, binary=False)
