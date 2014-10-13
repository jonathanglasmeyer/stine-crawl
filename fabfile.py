from fabric.api import *
import os
from fabric.contrib.files import exists

project_name = os.path.basename(os.getcwd())
repo = 'https://github.com/jonathanewerner/' + project_name

env.use_ssh_config = True
env.hosts = ['ocean']

def dispatcher():
    run('nginx-dispatcher.sh')

def push():
    local("git push")

def run_app():
    run("fig up -d")

def deploy():
    push()
    code_dir = 'dev/' + project_name
    with settings(warn_only=True):
        if run("test -d %s" % code_dir).failed:
            run("git clone {} {} --depth=1".format(repo, code_dir))
    with cd(code_dir):
        run('git reset --hard')
        run("git pull")
        run_app()

def path():
    print()
