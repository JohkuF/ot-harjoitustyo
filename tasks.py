from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/main.py", pty=True)

@task
def test(ctx):
    ctx.run("coverage run -m pytest src/", pty=True)

@task
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)