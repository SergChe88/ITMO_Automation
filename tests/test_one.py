def test_fail():
#    assert 'test' == 'testing'
    assert not 'test' == 'testing'

def test_task_1():
    x = ['a', 'b', 'c']
    y = [1, 2, 3]
#    assert not x == y
    assert x != y
