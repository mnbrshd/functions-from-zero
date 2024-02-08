from mylib.bot import scrape
import click


@click.command()
@click.option("--name", help="Web page we want to scrape")
@click.option("--length", help="The length of the output from wikipedia")
def cli(name, length):
    result = scrape(name, length)
    click.echo(click.style(f"{result}", bg="white", fg="blue"))


if __name__ == "__main__":
    cli()
