from . import celery
import subprocess

import time
import os
import signal

from celery.contrib.abortable import AbortableTask





@celery.task(bind=True, base=AbortableTask)
def roscore(self):
    print 'starting...'
    proc = subprocess.Popen(['roscore'], preexec_fn=os.setpgrp)
    print 'started: ', proc.pid

    while not self.is_aborted():
        time.sleep(1)
    print 'killing roscore'

    os.killpg(os.getpgid(proc.pid), signal.SIGINT)
    print 'killed'


@celery.task(bind=True, base=AbortableTask)
def rosrun(self, package, node):
    print 'starting...'
    proc = subprocess.Popen(['rosrun', package, node], preexec_fn=os.setpgrp)
    print 'started: ', proc.pid

    while not self.is_aborted():
        time.sleep(1)
    print 'killing node'

    os.killpg(os.getpgid(proc.pid), signal.SIGINT)
    print 'killed'
