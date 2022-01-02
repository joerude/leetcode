# https://www.codewars.com/kata/55c6126177c9441a570000cc

# Weight for weight

def order_weight(strng):
    def summ (lst):
        c = 0
        for i in lst:
            c += int(i)
        return c

    out = sorted(strng.split(), key=lambda x:(summ(x), x))
    return ' '.join(out)



import codewars_test as test
    
@test.describe("Weight for weight")
def tests():
    @test.it("basic tests")
    def basics1():
        test.assert_equals(order_weight("103 123 4444 99 2000"), "2000 103 123 4444 99")
        test.assert_equals(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"), "11 11 2000 10003 22 123 1234000 44444444 9999")
        test.assert_equals(order_weight(""), "")
        