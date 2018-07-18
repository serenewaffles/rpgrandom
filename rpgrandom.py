import yaml
import random
import readline
import os
import click
import colorama
from colorama import Fore, Back, Style

stream=open(os.path.join(os.path.dirname(__file__), 'tables.yml'))
lists=yaml.load(stream)

contextSettings = dict(help_option_names=['-h', '--help'])
@click.group(context_settings=contextSettings)
#@click.option('--count', '-c', help='Number of items to generate', type=int, metavar='<count>', default=1, show_default=True)
@click.version_option(version='0.1', prog_name='RPG Random Generator')
def cli():
        pass

@cli.command()
@click.option('--local', '-l', 'eventScope', help='Roll a local event', is_flag=True, default=True, flag_value='local')
@click.option('--global', '-g', 'eventScope', help='Roll a global event', is_flag=True, flag_value='global')
@click.option('--type', '-t', 'eventType', help='Specify a type of event to roll', default='random', type=click.Choice(lists['local events']+lists['global events']+['random']), show_default=True)
def event(eventScope, eventType):
        """Roll an event. This will roll the event and all necessary components (i.e. if you roll an accident type event, an accident will be rolled for you)."""
        if eventType is 'random':
                table = eventScope + ' events'
                length = len(lists[table])-1
                choice = random.randint(0, length)
                click.echo(f"Rolling a {Fore.MAGENTA}{Style.BRIGHT}{eventScope.title()} Event{Style.RESET_ALL}")
                eventType = lists[table][choice].lower()
                click.echo(f"Your event is a(n) {Fore.GREEN}{eventType.title()}{Fore.RESET}")
        else:
                pass
        
        length = len(lists[eventType])-1
        choice = random.randint(0, length)
        click.echo(f"{Fore.GREEN}{lists[eventType][choice]['title']}{Fore.RESET}")
        click.echo(f"{lists[eventType][choice]['description']}")

        try:
                if type(lists[eventType][choice]['needed']) is list:
                        click.echo(f"{Fore.BLUE}{Style.BRIGHT}This will require:{Style.RESET_ALL}")
                        for x in lists[eventType][choice]['needed']:
                                click.echo(f"{Fore.MAGENTA}{Style.BRIGHT}A(n) {x}{Style.RESET_ALL}")
                                subchoice = random.randint(0, len(lists[x])-1)
                                click.echo(f"{lists[x][subchoice]}")
        except KeyError:
                pass

        try:
                if type(lists[eventType][choice]['optional']) is list:
                        click.echo(f"{Fore.BLUE}{Style.BRIGHT}You may wish to have:{Style.RESET_ALL}")
                        for x in lists[eventType][choice]['optional']:
                                click.echo(f"{Fore.MAGENTA}{Style.BRIGHT}A(n) {x}{Style.RESET_ALL}")
                                subchoice = random.randint(0, len(lists[x])-1)
                                click.echo(f"{lists[x][subchoice]}")
        except KeyError:
                pass

#@cli.command()
def survivor():
        """Roll a survivor. This will not roll any NPC details."""
        print("a survivor")

@cli.command()
@click.option('--male', '-m', 'npcSex', help='Roll a male NPC', is_flag=True)
@click.option('--female', '-f', 'npcSex', help='Roll a female NPC', is_flag=True)
@click.option('--type', '-t', 'npcType', help='Specify a type of NPC to roll', default='random', type=click.Choice(lists['npcs']+['random']), show_default=True)
def npc(npcSex):
        """Roll an NPC. This will generate a person, but no stats. The gender only affects the name list used. If no gender is supplied, then both namelists are used."""
        print("an NPC (details coming soon!)")