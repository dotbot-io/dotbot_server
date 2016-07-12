from . import celery
import subprocess

@celery.task()
def roscore():
    subprocess.call(['roscore'])

@celery.task()
def rosrun(package, node):
    subprocess.call(['rosrun', package, node])
