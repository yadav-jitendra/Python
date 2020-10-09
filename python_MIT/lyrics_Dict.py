# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 10:17:41 2016

@author: WELG
"""


def lyrics_to_frequencies(lyrics):
    myDict = {}
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict


yesterday_beettles = ['Yesterday', 'All', 'my', 'troubles',
                      'seemed', 'so', 'far', 'away', 'Now', 'it', 'looks', 'as',
                      'though', "they're", 'here', 'to', 'stay', 'Oh,', 'I', 'believe',
                      'in', 'yesterday', 'Suddenly', "I'm", 'not', 'half', 'the', 'man',
                      'I', 'used', 'to', 'be', "There's", 'a', 'shadow', "hangin'", 'over',
                      'me', 'Oh,', 'yesterday', 'came', 'suddenly', 'Why', 'she', 'had', 'to', 'go,',
                      'I', "don't", 'know,', 'she', "wouldn't", 'say', 'I', 'said', 'something', 'wrong,',
                      'now', 'I', 'long', 'for', 'yesterday', 'Yesterday', 'Love', 'was', 'such', 'an', 'easy',
                      'game', 'to', 'play', 'Now', 'I', 'need', 'a', 'place', 'to', 'hide', 'away', 'Oh,', 'I',
                      'believe', 'in', 'yesterday', 'Why', 'she', 'had', 'to', 'go,', 'I', "don't", 'know,',
                      'she', "wouldn't", 'say', 'I', 'said', 'something', 'wrong,', 'now', 'I', 'long',
                      'for', 'yesterday', 'Yesterday', 'Love', 'was', 'such', 'an', 'easy', 'game', 'to',
                      'play', 'Now', 'I', 'need', 'a', 'place', 'to', 'hide', 'away', 'Oh,', 'I', 'believe',
                      'in', 'yesterday', 'Mm', 'mm', 'mm', 'mm', 'mm', 'mm', 'mm']




she_loves_you = ['she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
                 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
                 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',

                 'you', 'think', "you've", 'lost', 'your', 'love',
                 'well', 'i', 'saw', 'her', 'yesterday-yi-yay',
                 "it's", 'you', "she's", 'thinking', 'of',
                 'and', 'she', 'told', 'me', 'what', 'to', 'say-yi-yay',

                 'she', 'says', 'she', 'loves', 'you',
                 'and', 'you', 'know', 'that', "can't", 'be', 'bad',
                 'yes', 'she', 'loves', 'you',
                 'and', 'you', 'know', 'you', 'should', 'be', 'glad',

                 'she', 'said', 'you', 'hurt', 'her', 'so',
                 'she', 'almost', 'lost', 'her', 'mind',
                 'and', 'now', 'she', 'says', 'she', 'knows',
                 "you're", 'not', 'the', 'hurting', 'kind',

                 'she', 'says', 'she', 'loves', 'you',
                 'and', 'you', 'know', 'that', "can't", 'be', 'bad',
                 'yes', 'she', 'loves', 'you',
                 'and', 'you', 'know', 'you', 'should', 'be', 'glad',

                 'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
                 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
                 'with', 'a', 'love', 'like', 'that',
                 'you', 'know', 'you', 'should', 'be', 'glad',

                 'you', 'know', "it's", 'up', 'to', 'you',
                 'i', 'think', "it's", 'only', 'fair',
                 'pride', 'can', 'hurt', 'you', 'too',
                 'pologize', 'to', 'her',

                 'Because', 'she', 'loves', 'you',
                 'and', 'you', 'know', 'that', "can't", 'be', 'bad',
                 'Yes', 'she', 'loves', 'you',
                 'and', 'you', 'know', 'you', 'should', 'be', 'glad',

                 'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
                 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
                 'with', 'a', 'love', 'like', 'that',
                 'you', 'know', 'you', 'should', 'be', 'glad',
                 'with', 'a', 'love', 'like', 'that',
                 'you', 'know', 'you', 'should', 'be', 'glad',
                 'with', 'a', 'love', 'like', 'that',
                 'you', 'know', 'you', 'should', 'be', 'glad',
                 'yeah', 'yeah', 'yeah',
                 'yeah', 'yeah', 'yeah', 'yeah'
                 ]

beatles = lyrics_to_frequencies(yesterday_beettles)


def most_common_words(freqs):
    values = freqs.values()
    best = max(freqs.values())
    words = []
    for k in freqs:
        if freqs[k] == best:
            words.append(k)
    return (words, best)


def words_often(freqs, minTimes):
    result = []
    done = False
    while not done:
        temp = most_common_words(freqs)
        if temp[1] >= minTimes:
            result.append(temp)
            for w in temp[0]:
                del (freqs[w])  # remove word from dictionary
        else:
            done = True
    return result


print(words_often(beatles, 2))
