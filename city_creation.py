import random
import string
class list_Check:
    def __init__(self):
        self.lst = []
        for i in range(10):
            var = random.choice(string.ascii_uppercase)
            while True:
                if var in self.lst:
                    var = random.choice(string.ascii_uppercase)
                else:
                    self.lst.append(var)
                    break
        var = self.lst[0]
        self.lst.append(var)
        # print(self.lst)

cc = list_Check()

# x = 0
# for i in cc.lst:
#     if i in cc.lst[cc.lst.index(i)+1:]:
#         print(i)
