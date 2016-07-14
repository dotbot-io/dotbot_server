from . import app

from subprocess import call
from celery.contrib.methods import task_method
import celery

import tasks


class Master:
    def __init__(self):
        self._process = None
        print 'created'

    def run(self):
        print self._process
        self._process = tasks.roscore.delay()

    def kill(self):
        print self._process
        if self._process is not None:
            print "terminating"
            self._process.abort()

class Node:
    def __init__(self, package, node):
        self._process = None
        self._package = package
        self._node = node

    def run(self):
        self._process = tasks.rosrun.delay(self._package, self._node)
        print self._process

    def kill(self):
        print self._process
        if self._process is not None:
            print "terminating"
            self._process.abort()

class Launch:
    def __init__(self, package, launchfile):
        self._process = None
        self._package = package
        self._launchfile = launchfile

    def run(self):
        self._process = tasks.roslaunch.delay(self._package, self._launchfile)
        print self._process

    def kill(self):
        print self._process
        if self._process is not None:
            print "terminating"
            self._process.abort()
