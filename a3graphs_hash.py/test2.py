

import random
from nltk.corpus import stopwords
import string
import re
x = [['supplement', 2], ['lead', 1], ['specific', 2], ['incomplete', 1], ['also', 1], ['plagiarism', 1], ['valuable', 1], ['tool', 1], ['used', 1], ['best', 2], ['proper',
                                                                                                                                                                  1], ['following', 1], ['questions', 5], ['practices', 1], ['relevant', 1], ['completing', 1], ['enhance', 1], ['using', 2], ['verify', 2], ['achieve', 1], ['success', 1], ['pasting', 1], ['effort', 1], None, None, None, None, None, ['integrity', 1], None, None, ['learning', 3], None, ['conclusion', 1], None, ['obtained', 2], None, ['response', 3], ['due', 1], ['paraphrase', 1], ['quality', 1], ['reputable', 1], ['check', 2], ['limitations', 1], ['serious', 1], ['source', 2], ['helpful', 1], ['broad', 1], ['ask', 2], ['evaluate', 1], ['use', 6], ['sources', 2], ['openended', 1], ['get', 1], ['critically', 1], ['consider', 3], ['biases', 1], ['copying', 1], ['words', 2], ['research', 3], ['attribution', 1], ['chatgpt', 12], ['cite', 1], ['generating', 1], ['without', 2], ['sole', 1], ['may', 1], ['finally', 1], ['implications', 2], ['answering', 1], ['results', 1], ['information', 5], ['responses', 1], ['accuracy', 1], ['important', 2], ['resource', 1], ['clear', 2], ['irrelevant', 1], ['provided', 1], ['academic', 3], ['present', 1], ['offense', 1], ['assignments', 2], ['complete', 1], ['analyze', 1], ['putting', 1], ['avoid', 1], ['relevance', 1], ['assignment', 4], ['necessary', 1], ['undermine', 1], ['process', 1], ['content', 1], ['receiving', 1], ['responsible', 2], ['sure', 1], ['manner', 2], ['give', 1], ['ethical',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       4], ['credit', 2]]


class ClosedHashtable:

    def __init__(self):
        self.hashsize = 100
        self.table = [None]*self.hashsize
        self.stop_words = set(stopwords.words('english'))
        self.words = []

        self.p2_hashsize = 51
        self.p2_table = [None]*self.p2_hashsize

    def fileloader(self, filepath):
        self.root = None
        words = self.parse_file(filepath)
        for word in words:
            self.words.append(word)

    def parse_file(self, filepath):
        with open(filepath, 'r') as f:
            textfile = f.readlines()
            words = []
            for line in textfile:
                # textfile is now a string of the text file
                line = line.strip().lower()
                # seperated each line via periods
                line = line.translate(
                    str.maketrans('', '', string.punctuation))
                # eliminated periods
                line = self.remove_stopwords(line)
                # got rid of redudent terms such as the, this, is ETC

                line = re.sub('\d+', '', line)
                line = re.sub(' +', ' ', line)
                # now put into list form
                if line:
                    words.extend(line.split(" "))
            return words

    def remove_stopwords(self, text):
        return " ".join([word for word in str(text).split() if word not in self.stop_words])

    def check(self):
        x = [['supplement', 2], ['lead', 1], ['specific', 2], ['incomplete', 1], ['also', 1], ['plagiarism', 1], ['valuable', 1], ['tool', 1], ['used', 1], ['best', 2], ['proper',
                                                                                                                                                                          1], ['following', 1], ['questions', 5], ['practices', 1], ['relevant', 1], ['completing', 1], ['enhance', 1], ['using', 2], ['verify', 2], ['achieve', 1], ['success', 1], ['pasting', 1], ['effort', 1], None, None, None, None, None, ['integrity', 1], None, None, ['learning', 3], None, ['conclusion', 1], None, ['obtained', 2], None, ['r', 1], ['ask', 2], ['evaluate', 1], ['use', 6], ['sources', 2], ['openended', 1], ['get', 1], ['critically', 1], ['consider', 3], ['biases', 1], ['copying', 1], ['words', 2], ['research', 3], ['attribution', 1], ['chatgpt', 12], ['cite', 1], ['generating', 1], ['without', 2], ['sole', 1], ['may', 1], ['finally', 1], ['implications', 2], ['answering', 1], ['results', 1], ['information', 5], ['responses', 1], ['accuracy', 1], ['important', 2], ['resource', 1], ['clear', 2], ['irrelevant', 1], ['provided', 1], ['academic', 3], ['present', 1], ['offense', 1], ['assignments', 2], ['complete', 1], ['analyze', 1], ['putting', 1], ['avoid', 1], ['relevance', 1], ['assignment', 4], ['necessary', 1], ['undermine', 1], ['process', 1], ['content', 1], ['receiving', 1], ['responsible', 2], ['sure', 1], ['manner', 2], ['give', 1], ['ethical',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        4], ['credit', 2]]
        list = []
        for i in x:
            for j in obj.words:
                try:

                    if i[0] == j and i not in list:

                        list.append(i)
                except:
                    ('none')
        print(list)
        print(len(list))


obj = ClosedHashtable()
obj.fileloader('D:/A3test.txt')

obj.check()
