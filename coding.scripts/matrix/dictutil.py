# Copyright 2013 Philip N. Klein
def dict2list(dct, keylist): return [ dct.get(x) for x in keyList ]


def list2dict(L, keylist): return{ keylist[index]:L[index] for index in range(0,len(L))}

def listrange2dict(L): return [ i:L[i] for i in L ]