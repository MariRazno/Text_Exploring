import nltk
from nltk import sent_tokenize
from nltk import word_tokenize
from nltk.text import  Text
from nltk.stem import *
nltk.download('averaged_perceptron_tagger')

yellow_raw_text = open(r"C:\git_project\summer-school-2019\classes\4_corpora\data\king_in_yellow.txt", "r").read()
yellow_raw_text_paragraphs = yellow_raw_text.splitlines()
print(yellow_raw_text_paragraphs[:3])
yellow_raw_text_sentences = sent_tokenize(yellow_raw_text)
print(yellow_raw_text_sentences[:3])
yellow_raw_text_words = word_tokenize(yellow_raw_text)
print(yellow_raw_text_words[:9])
yellow_corpus = Text(yellow_raw_text_words)
print(yellow_corpus)
yellow_corpus.concordance("started")

stemmer = porter.PorterStemmer()


class IndexedText(object):

    def __init__(self, stemmer, text):
        self._text = text
        self._stemmer = stemmer
        self._index = nltk.Index((self._stem(word), i)
                                 for (i, word) in enumerate(text))

    def concordance(self, word, width=40):
        key = self._stem(word)
        wc = int(width/2)
        idx = self._index[key]
        if len(idx) > 0:
            for i in self._index[key]:
                lcontext = ' '.join(self._text[i-wc:i])
                rcontext = ' '.join(self._text[i:i+wc])
                ldisplay = '{:>{width}}'.format(lcontext[-width:], width=width)
                rdisplay = '{:{width}}'.format(rcontext[:width], width=width)
                print(ldisplay, rdisplay)

    def _stem(self, word):
        return self._stemmer.stem(word).lower()

indexed_by_stemmer = IndexedText(nltk.PorterStemmer(),yellow_corpus)
indexed_by_stemmer.concordance("start", width=15)
wnl = nltk.WordNetLemmatizer()

words = [('Time', 'NNP'),
 ('flies', 'NNS'),
 ('like', 'IN'),
 ('an', 'DT'),
 ('arrow', 'NN'),
 ('.', '.')]


def convert_pos_tag(treebank_tag):
    if treebank_tag.startswith('J'):
        return 'a'
    elif treebank_tag.startswith(('V', 'MD')):
        return 'v'
    elif treebank_tag.startswith('N'):
        return 'n'
    else:
        return 'r'

for i in yellow_raw_text_words:
    def get_wordnet_pos(i):
        return convert_pos_tag(nltk.pos_tag([i])[0][1])
