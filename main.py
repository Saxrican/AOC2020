
from common.common import loadData

from day1.day1 import function1, function2
print("day 1 part 1 = "+str(function1(loadData("day1", parseInt=True))))
print("day 1 part 2 = "+str(function2(loadData("day1", parseInt=True))))

import day2.day2
print("day 2 part 1 = "+str(len(day2.day2.function1(loadData("day2")))))
print("day 2 part 2 = "+str(len(day2.day2.function2(loadData("day2")))))
