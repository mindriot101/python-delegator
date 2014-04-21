import types

class Delegator(object):
    def __init__(self, delegatee, **kwargs):
        self.delegatee = delegatee
        
        for key in kwargs:
            m = types.MethodType(kwargs[key], self)
            setattr(self, key, m)

    def __getattr__(self, name):
        return getattr(self.delegatee, name)
