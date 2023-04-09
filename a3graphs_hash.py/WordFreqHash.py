import re
import string
from nltk.corpus import stopwords
import random


class ClosedHashtable:

    def __init__(self):
        self.hashsize = 51
        self.table = [None]*self.hashsize
        self.stop_words = set(stopwords.words('english'))
        self.words = []

        # max of 50 words in the part 2 section, hence size of 51
        self.p2_hashsize = 50
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

    def hashfunc(self, word):
        total = 0

        for i in range(len(word)):
            total = total + (i+1) * ord(word[i])

        total = total % self.hashsize
        return total

    def add(self, words):
        for word in words:
            slot = self.hashfunc(word)
            start = slot
            insert = False
            while insert == False:

                if self.table[slot] is None:
                    self.table[slot] = [word, 1]
                    insert = True
                    break
                elif word == self.table[slot][0]:
                    self.table[slot][1] += 1
                    insert = True
                    break
                slot = (slot+1) % self.hashsize
                if slot == start:
                    insert = True
                    break

        "---part2------------------------------------------------------"

    def p2_hashfunc(self, word):
        total = 0

        for i in range(len(word)):
            total = total + (i+1) * ord(word[i])

        total = total % self.p2_hashsize
        return total

    def p2_add(self, words):
        for word in words:
            slot = self.p2_hashfunc(word)
            start = slot
            insert = False
            while insert == False:
                if self.p2_table[slot] is None:
                    self.p2_table[slot] = [word, 1]
                    insert = True
                    break
                elif word == self.p2_table[slot][0]:
                    self.p2_table[slot][1] += 1
                    insert = True
                    break
                slot = (slot+1) % self.p2_hashsize
                if slot == start:
                    insert = True
                    break

    def p2_search(self):
        print(self.p2_table)
        for k in range(5, 25, 5):
            print("k =", k*2)
            print("")
            list = []
            for i in range(k):
                x = random.randint(0, len(self.p2_table)-1)
                list.append(self.p2_table[x][0])
                x = "notinlist"
                list.append(x)
            for i in list:
                steps = 0
                for j in range(len(self.p2_table)):
                    steps += 1
                    try:
                        if steps == len(self.p2_table)+1:
                            print(i, "is not in the table")
                            break
                        if i == self.p2_table[j][0]:
                            print(i, "is in the table, steps= ", steps)
                            break
                    except:
                        pass


obje = ClosedHashtable()


obje.fileloader('D:/A3test.txt')
# obje.add(obje.words)
# obje.p2_add(obje.words)
# obje.p2_search()


class Node:

    def __init__(self, data, freq):
        self.data = data
        self.next = None
        self.freq = freq


class OpenHashtable:

    def __init__(self,):
        self.hashsize = 5
        self.hashtable = []
        self.stop_words = set(stopwords.words('english'))
        self.words = []
        # size of 50 for part 2 due to max hashtable size being 50
        self.p2_hashsize = 50
        self.p2_hashtable = []

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

    def hashfunc(self, word):
        total = 0

        for i in range(len(word)):
            total = total + (i+1) * ord(word[i])

        total = total % self.hashsize
        print(total)
        return total

    def construct(self):
        for i in range(self.hashsize):
            add = Node('Head')
            self.hashtable.append([add])
            # print(self.hashtable[i][0].data)

    # adds to hash table
    def add(self):
        for word in self.words:
            new_node = Node(word)
            # get correct slot
            slot = self.hashfunc(word)
            # set current to the first node in the slot
            curr = self.hashtable[slot][0]
            done = False
            # if the first node is empty, add the new node
            while done == False:
                if curr.next == None and curr.data != new_node.data:
                    curr.next = new_node
                    done = True
                # add to word frequency if the word is already in the hashtable
                elif curr.data == new_node.data:
                    curr.freq += 1
                    done = True
                # traverse
                curr = curr.next

    # prints the hashtable

    def print(self):
        for i in range(self.hashsize):
            print("index", i)
            # set current to the first node in the slot
            curr = self.hashtable[i][0]
            # traverse
            list = []
            while curr != None:
                x = curr.data, curr.freq
                list.append(x)
                # print(curr.data, curr.freq)
                curr = curr.next
            print(list)

    """ -------------------- PART 2 ------------------------------------------------------------"""

    def construct2(self):
        for i in range(self.p2_hashsize):
            add = Node('Head', 0)
            self.p2_hashtable.append([add])
            # print(self.hashtable[i][0].data)

    def add2(self):
        for word in self.words:
            new_node = Node(word, 1)
            # get correct slot
            slot = self.hashfunc2(word)
            # set current to the first node in the slot
            curr = self.p2_hashtable[slot][0]
            done = False
            # if the first node is empty, add the new node
            while done == False:
                if curr.next == None and curr.data != new_node.data:
                    curr.next = new_node
                    done = True
                # add to word frequency if the word is already in the hashtable
                elif curr.data == new_node.data:
                    curr.freq += 1
                    done = True
                # traverse
                curr = curr.next

    def search2(self):
        """"""
        for k in range(5, 25, 5):
            print("k =", k*2)
            print("")
            list = []
            for i in range(k):
                x = random.choice(self.words)
                list.append(x)
                x = "notinlist"
                list.append(x)
            print(list)

    def print2(self):
        for i in range(self.p2_hashsize):
            print("index", i)
            # set current to the first node in the slot
            curr = self.p2_hashtable[i][0]
            # traverse
            list = []
            while curr != None:
                x = curr.data, curr.freq
                list.append(x)
                # print(curr.data, curr.freq)
                curr = curr.next
            print(list)

    def hashfunc2(self, word):
        total = 0

        for i in range(len(word)):
            total = total + (i+1) * ord(word[i])

        total = total % self.p2_hashsize
        print(total)
        return total

    def main(self):
        obj.fileloader('D:/A3test.txt')
        obj.construct()
        obj.add()
        obj.print()

    def main2(self):
        obj2.fileloader('D:/A3test.txt')
        obj2.construct2()
        obj2.add2()
        # obj2.print2()
        obj2.search2()


obj = OpenHashtable()
# obj.main()
obj2 = OpenHashtable()
obj2.main2()

# for part 2) make size 51 because the most that will be in the hashtable is 50, due to K words being at most 50 in our case
