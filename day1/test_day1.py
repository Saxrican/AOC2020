from day1 import function1, function2

testData = [1721,979,366,299,675,1456]

def test_function1():
    assert function1(testData) == 514579

def test_function2():
    assert function2(testData) == 241861950