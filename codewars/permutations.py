#  https://www.codewars.com/kata/5254ca2719453dcc0b00027d

#  Permutations


def permutations(string):
    import itertools
    data = list(set(itertools.permutations(string)))
    return [''.join(list(i)) for i in data]

    
import codewars_test as test

test.assert_equals(sorted(permutations('a')), ['a']);
test.assert_equals(sorted(permutations('ab')), ['ab', 'ba'])
test.assert_equals(sorted(permutations('aabb')), ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])