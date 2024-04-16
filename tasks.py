from subprocess import call
from sys import platform
from invoke import task

@task
def build(ctx):
    if platform == "win32":
        ctx.run("py src/initialize_database.py")
    else:
        ctx.run("python3 src/initialize_database.py", pty=True)

@task
def start(ctx):
    if platform == "win32":
        ctx.run("py src/index.py")
    else:
        ctx.run("python3 src/index.py", pty=True)


@task
def coverage(ctx):
    if platform == "win32":
        ctx.run("coverage run --branch -m pytest src")
    else:
        ctx.run("coverage run --branch -m pytest src", pty=True)

@task(pre=[coverage])
def coverage_report(ctx):
    ctx.run("coverage html")
    if platform != "win32" and platform != "darwin":
        call(("xdg-open", "htmlcov/index.html"))

@task
def test(ctx):
    ctx.run("pytest src")

@task
def lint(ctx):
    ctx.run("pylint src")
