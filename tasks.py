from invoke import task
from subprocess import call
from sys import platform


@task
def foo(ctx):
    print("bar")
    
@task
def start(ctx):
    ctx.run("python3 src/index.py")
    
    
@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src")

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html")
    if platform != "win32":
        call(("xdg-open", "htmlcov/index.html"))