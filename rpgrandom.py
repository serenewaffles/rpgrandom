import yaml
import random
import readline
import os
import click
import colorama
from colorama import Fore, Back, Style

try:
    stream=open(os.path.join(os.path.dirname(__file__), 'tables.yml'))
    lists=yaml.load(stream)
except Exception:
    click.echo(f"{Fore.RED}{Style.BRIGHT}Unable to find tables.yml!{Style.RESET_ALL}")
    exit()

contextSettings = dict(help_option_names=['-h', '--help'])
@click.group(context_settings=contextSettings)
@click.version_option(version='0.1', prog_name='RPG Random Generator')
def cli():
        pass

@cli.command()
@click.option('--local', '-l', 'eventScope', help='Roll a local event', is_flag=True, default=True, flag_value='local')
@click.option('--global', '-g', 'eventScope', help='Roll a global event', is_flag=True, flag_value='global')
@click.option('--type', '-t', 'eventType', help='Specify a type of event to roll', default='random', type=click.Choice(lists['local events']+lists['global events']+['random']), show_default=True)
def event(eventScope, eventType):
        """Roll an event. This will roll the event and all necessary components (i.e. if you roll an accident type event, an accident will be rolled for you)."""
        
        occurence = {}
        
        if eventType is 'random':
                table = eventScope + ' events'
                eventType = random.choice(lists[table]).lower()
                click.echo(f"Rolling a {Fore.MAGENTA}{Style.BRIGHT}{eventScope.title()} Event{Style.RESET_ALL}")
                click.echo(f"Your event is a(n) {Fore.GREEN}{eventType.title()}{Fore.RESET}")
        else:
                pass
        
        occurence = lists[eventType][random.choice(list(lists[eventType].keys()))]
        click.echo(f"{Fore.GREEN}{occurence['title']}{Fore.RESET}")
        click.echo(f"{occurence['description']}")

        try:
                if type(occurence['needed']) is list:
                        click.echo(f"{Fore.BLUE}{Style.BRIGHT}This will require:{Style.RESET_ALL}")
                        for x in occurence['needed']:
                                click.echo(f"{Fore.MAGENTA}{Style.BRIGHT}A(n) {x}{Style.RESET_ALL}")
                                click.echo(f"{random.choice(lists[x])}")
        except KeyError:
                pass

        try:
                if type(occurence['optional']) is list:
                        click.echo(f"{Fore.BLUE}{Style.BRIGHT}You may wish to have:{Style.RESET_ALL}")
                        for x in occurence['optional']:
                                click.echo(f"{Fore.MAGENTA}{Style.BRIGHT}A(n) {x}{Style.RESET_ALL}")
                                click.echo(f"{random.choice(lists[x])}")
        except KeyError:
                pass

if __name__ == '__main__':
    cli()