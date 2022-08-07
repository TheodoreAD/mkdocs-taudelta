from invoke import task


@task
def output_requirements(c):
    c.run("poetry export -o requirements.txt --without-hashes")
