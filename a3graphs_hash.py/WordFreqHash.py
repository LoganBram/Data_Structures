import re
import string
from nltk.corpus import stopwords
import random
import unittest
import os

"""Test cases for my code, use: python -m unittest test_file_name.py in terminal"""


class ClosedHashtable:

    def __init__(self):
        self.hashsize = 100
        self.table = [None]*self.hashsize
        self.stop_words = set(stopwords.words('english'))
        self.words = []

        # max of 50 words being searched for in the part 2 section due to k <= 50, hence hashtablesize of 50
        # Yes, it doesnt include all the words within the textfile, but it only includes the exact amount words necessary

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
        print("CLOSED HASH TABLE p1 of size: ", self.hashsize)
        print("")
        print(self.table)
        print("")
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
        print("---------------CLOSED HASH TABLE p2 of size: ", self.p2_hashsize)
        print("")
        print(self.p2_table)

    def p2_searchtest(self):
        # searching function for closded hash table
        # starts at step = 1, because im counting going to the hashing index as a step
        for k in range(5, 30, 5):
            print("")
            print("k =", k*2)
            print("")
            # list of words we will look for
            list = []
            # add k*2 words to list since in my loop k is half of the actual k
            for i in range(k):
                # allows me to add one word in the table and one word not in the table
                x = random.randint(0, len(self.p2_table)-1)
                list.append(self.p2_table[x][0])
                x = "notinlist"+str(i)
                list.append(x)
            # iterate through words in our list to find
            for word in list:
                slot = self.p2_hashfunc(word)
                print("searching for: ", word, ", starting at index: ", slot)
                start = slot
                found = False
                steps = 1
                while found == False:
                    if word == self.p2_table[slot][0]:
                        found = True
                        print(word, "is in the table, after", steps, "steps")
                        print("")
                        break
                    slot = (slot+1) % self.p2_hashsize
                    steps += 1
                    # if done full loop and not found, then not in table
                    if slot == start:
                        found = True
                        print(word, "is not in the table -1")
                        print("")
                        break


obje = ClosedHashtable()
obje.fileloader('D:/A3test.txt')
obje.add(obje.words)
obje.p2_add(obje.words)
obje.p2_searchtest()


"-----OPEN HASH TABLE----------------"


class Node:

    def __init__(self, data, freq):
        self.data = data
        self.next = None
        self.freq = freq


class OpenHashtable:

    def __init__(self,):
        # NOTE: while coding i changed some things to cater towards pt2, hence the seperate functions for p1 and p2
        # but im realizing now alot of it wasnt necessary, regardless it still follows the instructions correctly
        # just harder to read
        self.hashsize = 13
        self.hashtable = []
        self.stop_words = set(stopwords.words('english'))
        self.words = []

        # max amount of values being stored is 50, so having around 4 per bucket on avg seems optimum to avoid any values having their own bucket
        self.p2_hashsize = 13
        self.p2_hashtable = []
        self.p2_words = []

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
        # using same hash function through entirety of code as introduced by the slides in class
        total = 0
        for i in range(len(word)):
            total = total + (i+1) * ord(word[i])

        total = total % self.hashsize

        return total

    def construct(self):
        for i in range(self.hashsize):
            add = Node('Head', 0)
            self.hashtable.append([add])
            # print(self.hashtable[i][0].data)

    # adds to hash table
    def add(self):
        for word in self.words:
            new_node = Node(word, 1)
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
        print("--------------OPEN HASHTABLE Using LinkedList Part 1-------")
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

    """ -------------------- PART 2 for open ------------------------------------------------------------"""

    def construct2(self):
        for i in range(self.p2_hashsize):
            add = Node('Head', 0)
            self.p2_hashtable.append([add])

    def add2(self):

        # gets 50 random words from the list of all the words in the text file
        for i in range(50):
            x = random.randint(0, len(self.words)-1)
            self.p2_words.append(self.words[x])
        # iterates through the chosen words and adds them to the hashtable
        for word in self.p2_words:
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

    # conducts search for pt 2 w/ helper function
    def search2(self):

        for k in range(5, 25, 5):
            print(" going to index counts as a step, lowest steps possible as per my definition is 3 due to head node")
            print("k =", k*2)
            print("")
            list = []
            # adds words to list following assignment instructions
            for i in range(k):
                x = random.choice(self.p2_words)
                list.append(x)
                x = "notinlist"
                list.append(x)
                # iterates through each word we are looking for and sends it to be searched
            for i in list:
                self.searchhelper2(i)

    # takes word from search list as input and searches for it in the hashtable
    def searchhelper2(self, word):
        # start steps at 1 because im counting going to correct bucket as a step
        # an item cannot have less then 3 steps due to first step being going to correct bucket, and first item in bucket being head placeholder
        # therefore requiring 3 steps to get to the first possible node of any of the buckets
        steps = 1
        found = False
        slot = self.hashfunc2(word)
        curr = self.p2_hashtable[slot][0]
        while curr != None:
            if curr.data == word:
                steps += 1
                print("found", word, "in", steps, "steps")
                print("")
                found = True
                break
            else:
                steps += 1
                curr = curr.next
                if curr == None:
                    print("not found", word, "-1")
                    print("")
                    break

    def hashfunc2(self, word):
        total = 0

        for i in range(len(word)):
            total = total + (i+1) * ord(word[i])

        total = total % self.p2_hashsize

        return total

    # prints out the hashtable
    def print2(self):
        print("")
        print("----------OPEN Hashtable for part 2------")
        print(" going to index counts as a step, lowest steps possible as per my definition is 3 due to head node")
        for i in range(self.p2_hashsize):
            print("")
            print("index", i)
            print("")
            # set current to the first node in the slot
            curr = self.p2_hashtable[i][0]
            # traverse
            list = []
            while curr != None:
                x = curr.data, curr.freq
                list.append(x)

                curr = curr.next
            print(list)

    def main(self):
        obj.fileloader('D:/A3test.txt')
        obj.construct()
        obj.add()
        obj.print()

    def main2(self):
        obj2.fileloader('D:/A3test.txt')
        obj2.construct2()
        obj2.add2()
        obj2.print2()
        obj2.search2()


obj = OpenHashtable()
obj.main()


obj2 = OpenHashtable()
obj2.main2()
