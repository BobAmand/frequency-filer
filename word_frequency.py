# Exercise 04; Word frequency Exercise
import re

# TODO - open + read sample.txt into current file.
# TODO - count the number of times each word is used net of capitalization
# TODO - identify the top 20 words and output them + count.
# TODO - run word_frequency_test, check pass/no pass.


def word_frequency(text):
    tot_text = re.sub(r'[^A-Za-z]', ' ', text, flags=0)    # punct removed
    iso_text = tot_text.split()                 # words split into list
    t_words = len(iso_text)            # Total word count net capitalization
    # print(tot_text)   #lots of data
    # print(iso_text)     #lots of data
    # print(t_words)      # 62,955 words


# create a list of unique numbers, pass 1
    u_words = []         # large volume of text
    for i in iso_text:              # NTS "i" is the word within iso_text.
        if i not in u_words:        # NTS changed to 'not in'
            u_words.append(i)       # NTS "i" is the word
    print(u_words)      # large volume of text data arrived.
# create a list of counts against the unique words.
    c_words = []        # empty
    for x in u_words:               # NTS altered u_words[x]
        iso_text.count(x)           # NTS "x" is the word
    print(c_words)      # empty!
# populate a dictionary by zipping the u_words[] and c_words[]
    w_dict = dict(zip(u_words, c_words))         # result is a dictionary
    print(w_dict)                   # empty!

# sort the dictionary by the value, high to low[becomes a list w tuples]:
    s_dict = sorted(w_dict.items(), key=lambda c: c[1], reverse=True)

# assembling the top 20:
    top_list = []
    for i in range(20):      # NTS reduced to 5 from 20 due to IndexError
        top_list.append(s_dict[i])      # NTS IndexError: list out of range
    print(top_list)                     # prints the top 20 list

    return w_dict                       # returns total dictionary to main()


def main():
    f = open("sample.txt")
    bee_text = ""                      # open string file to collect lines
    for line in f:
        bee_text += line               # concatenated lines into string
    word_frequency(bee_text)           # returns top_list
    close("sample.txt")
    # open(output.txt)

main()
