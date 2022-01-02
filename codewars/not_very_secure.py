# https://www.codewars.com/kata/526dbd6c8c0eb53254000110

# Not very secure


# test
import codewars_test as test

def alphanumeric(password):
    from string import punctuation
    punctuation = punctuation + '\n' + " " + ' ' + ''
    
    if all(i not in punctuation for i in password) and len(password) >= 1: 
        return True
    return False


@test.describe("Sample Tests")
def sample_tests():
    tests = [
        ("hello world_", False),
        ("PassW0rd", True),
        ("     ", False)
    ]
    for s, b in tests:
        @test.it('alphanumeric("' + s + '")')
        def sample_test():
            test.assert_equals(alphanumeric(s), b)