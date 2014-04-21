from delegator import Delegator

class Delegatee(object):
    def foo(self):
        return 10


def test_delegator_is_separate_object():
    d = Delegatee()
    a = Delegator(d)
    a.delegator_method = lambda: 10

    assert 'delegator_method' not in dir(d)
    assert 'delegator_method' in dir(a)

def test_delegator_passes_through():
    d = Delegatee()
    a = Delegator(d)

    assert a.foo() == 10

def test_delegator_can_override():
    d = Delegatee()
    a = Delegator(d, foo=lambda self: 5)

    assert a.foo() == 5

def test_custom_delegator():
    class NewDelegator(Delegator):
        def foo(self):
            return 5

    d = Delegatee()
    a = NewDelegator(d)

    assert a.foo() == 5

def test_delegator_has_access_to_delegatee():
    class NewDelegator(Delegator):
        def bar(self):
            return self.foo() + 5

    d = Delegatee()
    a = NewDelegator(d)

    assert a.bar() == 15

def test_delegator_has_access_in_constructor():
    d = Delegatee()
    a = Delegator(d, bar=lambda self: self.foo() + 5)

    assert a.bar() == 15
