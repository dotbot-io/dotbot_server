from . import app

from subprocess import call
from celery.contrib.methods import task_method

import tasks


class Master:
    def __init__(self):
        self._process = None

    def run(self):
        self._process = tasks.roscore.apply_async()

    def kill(self):
        if self._process is not None:
            self._process.revoke(terminate=True)

class Node:
    def __init__(self, package, node):
        self._process = None
        self._package = package
        self._node = node

    def run(self):
        self._process = tasks.rosrun.apply_async([self._package, self._node])

    def kill(self):
        if self._process is not None:
            self._process.revoke(terminate=True)
