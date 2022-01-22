# create a singleton class called MyTimer.
# this class will have all the singleton stuff.
# *etgar: add the following non-static methods: start_timer which will remember the current time,
# get_timer which will print the diff between the current time and the start time


# class name
class MyTimer(object):


    # cannot create more than one instance
    _instance = None

    # makes sure the __init__ won't work and we get the same object everytime
    def __init__(self):
        raise RuntimeError('Call instance() instead')


    def print_hello(self):
        print('hello')

    # need to complete in class