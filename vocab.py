import nltk
from nltk.corpus import wordnet
import re
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()


def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return None


vocab = set()
not_found_words = set()
counter = 0


def addToVocab(filename):
    global counter
    f = open(filename, "r")
    for line in f:
        line = line.lower()
        sent = re.sub('[\W_]+', ' ', line)
        wordsList = nltk.word_tokenize(sent)
        wordsList = [w for w in wordsList if not w in stop_words]
        tagged = nltk.pos_tag(wordsList)
        # print(tagged)
        for word in tagged:
            try:
                tag = get_wordnet_pos(word[1])
                if tag != None:
                    final_word = lemmatizer.lemmatize(word[0], pos=tag)
                    #print("word: ", word[0], "| root :", final_word)
                    vocab.add(final_word)
                else:
                    #print(word, " not found")
                    not_found_words.add(word)
                    counter += 1
            except:
                #print(word, " not found")
                not_found_words.add(word)
                counter += 1
        # #print(tagged)
    f.close()


addToVocab("love-quotes.txt")
addToVocab("comedy-quotes.txt")
addToVocab("tragedy-quotes.txt")

# print(not_found_words)
# print(len(vocab))
# print(counter)
# print(len(not_found_words))

"us" in vocab

vocab.add('warrior')
vocab.add('abuse')
vocab.add('vile')
vocab.add('hate')

# print(len(vocab))
