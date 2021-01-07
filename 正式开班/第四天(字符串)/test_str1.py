print("--------------------------------------------")
print("假设字符串类似这样的aba和aab就相等，现在随便给你二组字符串，请编程比较他们看是否相等")


def determineWhetherTheyAreEqual(a, b):
    a_set = set(list(a))
    b_set = set(list(b))
    if len(a) == len(b) and a_set == b_set:
        print("你们相等")
    else:
        print("不相等")

determineWhetherTheyAreEqual('ababcaea','caebbaa')