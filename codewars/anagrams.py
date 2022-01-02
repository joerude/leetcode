# https://www.codewars.com/kata/523a86aa4230ebb5420001e1

# Where my anagrams at?


def anagrams(word, words):
    
    word = ''.join(sorted(word))

    lst = [i for i in words if word == ''.join(sorted(i))]
    return lst