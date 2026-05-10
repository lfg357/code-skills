"""❌ 反例：命名晦涩、深层嵌套、隐式魔法"""
from typing import List

class DM:
    def __init__(self):
        self.d = {}

    def p(self, k, v):
        if k not in self.d:
            self.d[k] = []
        self.d[k].append(v)

    def g(self, k):
        return self.d.get(k, [])

def proc(data):
    m = DM()
    for i in range(len(data)):
        if data[i]["t"] == "u":
            if data[i].get("a"):
                m.p(data[i]["id"], data[i])
    r = []
    for k in m.d:
        if len(m.d[k]) > 0:
            s = 0
            for j in range(len(m.d[k])):
                s += m.d[k][j]["v"]
            r.append({"k": k, "s": s})
    return r
