from invoke import task
from subprocess import call
from sys import platform


@task
def foo(ctx):
    print("bar")
    
@task
def build(ctx):
    if platform == "win32":
        ctx.run("py src/initialize_database.py")
    else:
        ctx.run("python3 src/initialize_database.py")

@task
def start(ctx):
    if platform == "win32":
        ctx.run("py src/index.py")
    else:
        ctx.run("python3 src/index.py")
    
    
@task
def coverage(ctx):
    if platform == "win32":
        ctx.run("poetry run coverage run --branch -m pytest src")
    else:
        ctx.run("coverage run --branch -m pytest src")

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html")
    if platform != "win32":
        call(("xdg-open", "htmlcov/index.html"))