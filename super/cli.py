"""cli.py"""

import click

from super.standup import standup


@click.group()
def cli():
    """Start"""
    click.echo("Super!")


cli.add_command(standup)
