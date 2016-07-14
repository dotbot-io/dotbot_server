from . import celery
import subprocess

import time
import os
import signal

from celery.contrib.abortable import AbortableTask





@celery.task(bind=True, base=AbortableTask)
def roscore(self):
    print 'starting...'
    proc = subprocess.Popen(['roscore'])
    print 'started: ', proc.pid

    while not self.is_aborted():
        time.sleep(1)
    print 'killing roscore'

    proc.send_signal(signal.SIGINT)
    print 'killed'


@celery.task(bind=True, base=AbortableTask)
def rosrun(self, package, node):
    print 'starting...'
    proc = subprocess.Popen(['rosrun', package, node])
    print 'started: ', proc.pid

    while not self.is_aborted():
        time.sleep(1)
    print 'killing node'

    proc.send_signal(signal.SIGINT)
    print 'killed'

@celery.task(bind=True, base=AbortableTask)
def roslaunch(self, package, launchfile):
    print 'starting...'
    proc = subprocess.Popen(['roslaunch', package, launchfile])
    print 'started: ', proc.pid

    while not self.is_aborted():
        time.sleep(1)
    print 'killing node'

    proc.send_signal(signal.SIGINT)
    print 'killed'
