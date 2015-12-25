# Exercise 04; Word frequency Exercise
import re

# TODO - open + read sample.txt into current file.
# TODO - count the number of times each word is used net of capitalization
# TODO - identify the top 20 words and output them + count.
# TODO - run word_frequency_test, check pass/no pass.


def word_frequency(text):
    # remove punctuation, all lower case, and split into list:
    total_text = re.sub(r'[^A-Za-z]', ' ', text, flags=0).lower().split()
    total_words = len(total_text)        # Total word count
#     print("total words: {}".format(total_words))
#
# # create a list of unique words
#     unique_words = []         # large volume of text
#     for i in total_text:              # NTS "i" is the word within iso_text.
#         if i not in unique_words:        # NTS changed to 'not in'
#             unique_words.append(i)       # NTS "i" is the word
#
#     print("length of u_words: {}".format(len(unique_words)))
#     print("The first 10 unique words as a test:\n")
#     for i in range(0, 10):  # print a subset to verify list
#         print(unique_words[i], end=', ')
#     print('\n')


# create a list of word counts against the full text:
    count_words = {}
    for word in total_text:
        if word not in count_words:
            count_words[word] = 1
        else:
            count_words[word] += 1
    print("The top 20 words used in the text:\n")
    for k, v in sorted(count_words.items(),
                       key=lambda x: x[1],  # key on second col of tuple [0, 1]
                       reverse=True)[0:20]:  # reverse sort, top 20 only
        print(k, v)
    return count_words
    #  return count_words)

# # sort the dictionary by the value, high to low[becomes a list w tuples]:
#     s_dict = sorted(w_dict.items(), key=lambda c: c[1], reverse=True)


def main():
    f = open("sample.txt")
    bee_text = ""                      # open string file to collect lines
    for line in f:
        bee_text += line               # concatenated lines into string
    word_frequency(bee_text)           # returns top_list
    f.close()

'''
The word_frequency_test fails.  I think it is because my main() function
includes opening/closing the file.  The 'test' script is attempting to
put other text into the word_frequency() function and the current main()
is populating the function with "sample.txt".

Will come back and attempt to write an additional function to load data,
outside of the main() function.
'''

main()
