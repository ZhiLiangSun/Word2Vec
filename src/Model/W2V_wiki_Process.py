import logging
import os.path
import sys

from gensim.corpora import WikiCorpus

from src.Utils import Path

if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))

    # check and process input arguments

    if len(sys.argv) < 3:
        print
        globals()['__doc__'] % locals()
        sys.exit(1)
    inp, outp = sys.argv[1:3]
    space = " "
    i = 0
    DT_Path = os.path.join(Path.Data_Path + os.sep, 'raw_data', inp)
    Des_Path = os.path.join(Path.Data_Path + os.sep, 'parsed_data', outp)

    output = open(Des_Path, 'w', encoding='utf8')

    wiki = WikiCorpus(DT_Path, dictionary={})
    for text in wiki.get_texts():
        output.write(space.join(text) + "\n")
        i = i + 1
        if (i % 10000 == 0):
            logger.info("Saved " + str(i) + " articles")

    output.close()

    logger.info("Finished. Saved " + str(i) + " articles")
