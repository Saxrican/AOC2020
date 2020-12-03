from day2 import lineParse, function1, function2

testData = ["1-3 a: abcde","1-3 b: cdefg","2-9 c: ccccccccc"]

def test_lineParse():
    assert lineParse(testData[0]) == [1,3,'a',"abcde"]

def test_function1():
    assert len(function1(testData)) == 2

def test_function2():
    assert len(function2(testData)) == 1