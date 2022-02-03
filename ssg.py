import typer

from ssg.site import site

def main(soure="content", dest ="dist")
    config = {"source": source, "dest": dest}

    Site(**config).build()

typer.run(main)
