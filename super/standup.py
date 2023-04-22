"""standup.py"""
import click


@click.group()
def standup():
    """Standup commands"""
    click.echo("standup cli")


@standup.command()
def yesterday():
    """Ask the user what they completed on the previous work-day."""
    click.echo("what did you do yesterday?")


@standup.command()
def today():
    """Ask the user what they plan to accomplish today."""
    click.echo("what are you doing today?")


@standup.command()
def blockers():
    """Ask the user if their tasks are blocked."""
    click.echo("blockers?")
