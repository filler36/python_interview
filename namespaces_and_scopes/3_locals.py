def foo():
    a = 'local variable'
    print(locals())  # {'a': 'local variable'}

    """
    locals() returns only a copy of local namespace.
    Thus, a change of locals() dictionary will not affect a real local namespace
    """
    locals()['a'] = 'changed local variable'  #
    print(locals())  # {'a': 'local variable'}

foo()
