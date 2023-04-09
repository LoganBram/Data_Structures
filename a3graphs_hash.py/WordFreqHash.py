import re
import string
from nltk.corpus import stopwords


class ClosedHashtable:

    def __init__(self):
        self.hashsize = 100
        self.table = [None]*self.hashsize
        self.stop_words = set(stopwords.words('english'))
        self.words = []

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
            insert = False
            counter = slot

            # while the word has not been inserted
            while insert != True and counter < self.hashsize:
                # if slot is empty, insert word
                if self.table[counter] == None:
                    self.table[counter] = [word, 1]
                    insert = True
                    break
                # if word is same as word in slot, increment freq
                if self.table[counter][0] == word:
                    thing = self.table[counter]
                    thing[1] += 1
                    self.table[counter] = thing
                    insert = True
                    break
                # if counter + 1 = original has slot, it means loop of entire array completed, and table is full
                if counter + 1 == slot:
                    print("table is still full")
                    insert = True
                    break
                # if counter == hashsize - 1, it means we have reached the end of the array, so we need to wrap around
                # negative one because we increment counter at the end of the loop
                if counter == self.hashsize - 1:
                    counter = -1
                # Linear probe
                else:
                    counter += 1


# obje = ClosedHashtable()

# obje.fileloader('D:/A3test.txt')
# obje.add(obje.words)
# print(obje.table)

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.freq = 1


class OpenHashtable:

    def __init__(self,):
        self.hashsize = 5
        self.hashtable = []
        self.stop_words = set(stopwords.words('english'))
        self.words = []

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

    def main(self):
        obj.fileloader('D:/A3test.txt')
        obj.construct()
        obj.add()
        obj.print()


obj = OpenHashtable()
obj.main()
'''
obj.construct()
obj.add('asdf')
obj.add('asdfaas')
obj.add('asdfagfd')
obj.add('asdfaas')
obj.add('asdfaas')
'''
# obj.print()

# for part 2) make size 51 because the most that will be in the hashtable is 50, due to K words being at most 50 in our case
