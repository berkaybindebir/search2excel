from search import search_query
from folder import folder_setup
import click


@click.command()
@click.option('--page', default = 1, help = 'How Many Pages You Want')
@click.argument('query')
def start(query, page):
    click.echo("Please Wait..")
    
    results = search_query(query, page)
    click.echo(results)
    click.echo("="*200)
    click.echo("Do You Want Make a Excel File? [y/n]")
    a = click.getchar()
    click.echo()
    if a == "y":
        click.echo("Okay")
        folder_setup(results)
    elif a == "n":
        click.echo("Opss..")
    else:
        click.echo("Invalid Input, Please Type Yes or Not")

if __name__ == '__main__':
    start()