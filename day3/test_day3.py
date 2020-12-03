from day3 import function1, function2

testData = ["..##.......","#...#...#..",".#....#..#.","..#.#...#.#",".#...##..#.","..#.##.....",".#.#.#....#",".#........#","#.##...#...","#...##....#",".#..#...#.#"]

def test_function1():
    assert function1(testData, 3, 1) == 7

def test_function2():
    assert function2(testData, [[1,1],[3,1],[5,1],[7,1],[1,2]]) == 336