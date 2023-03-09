"""cli.py"""

import click


@click.group()
def standup():
    click.echo("standup cli")


@standup.command()
def yesterday():
    click.echo('what did you do yesterday?')


@standup.command()
def today():
    click.echo('what are you doing today?')


@standup.command()
def blockers():
    click.echo('blockers?')
