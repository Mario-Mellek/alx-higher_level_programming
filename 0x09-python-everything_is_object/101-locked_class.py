#!/usr/bin/python3
class LockedClass:
    """
    LockedClass: prevents the user from dynamically
    creating new instance attributes unless they're called:
    first_name
    """
    __slots__ = ["first_name"]

    def __init__(self):
        pass
