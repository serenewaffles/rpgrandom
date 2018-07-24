# rpgrandom

## Installation

1. The simpler way to install
   1. Download rpgrandom.py
   1. run `python rpgrandom.py [OPTIONS] COMMAND [ARGS]`
1. The simpler way to run
   1. Download rpgrandom.py and setup.py to a folder
   1. In that folder run `python -m pip install .`
   1. Run `rpgrandom [OPTIONS] COMMAND [ARGS]`

## Usage

`rpgrandom -h` will print out a dynamic help text showing what items are available to roll.

```rpgrandom -h
Usage: rpgrandom [OPTIONS] COMMAND [ARGS]...

Options:
  --version   Show the version and exit.
  -h, --help  Show this message and exit.

Commands:
  event  Roll an event.
```

`rpgrandom COMMAND -h` will print out a dynamic help text about a specific type of roll.

```rpgrandom event -h
Usage: rpgrandom event [OPTIONS]

  Roll an event. This will roll the event and all necessary components (i.e.
  if you roll an accident type event, an accident will be rolled for you).

Options:
  -l, --local                     Roll a local event
  -g, --global                    Roll a global event
  -t, --type [Accident|Festival|Civil war|Industrial disaster|Invasion|Natural disaster|Failed experiment|Zombie apocalypse|random]
                                  Specify a type of event to roll  [default:
                                  random]
  -h, --help                      Show this message and exit.
```

## Data storage

The script requires a table.yml file in the same directory as the script.
The YAML file should have the following format

```yaml
global events:
  # A list of global event types. Each of these should have a corresponding entry below.
  - zombie apocalypse
local events:
  # A list of local event types. Each of these should also have an entry below.
  - industrial disaster
  - fire
npcs:
  # A list of NPC types.
  - villain
  - ally
names:
  # A list of name origins.
  - chinese
  - english

# This lists the different specific events that could fall under
# each type of local or global event above. When an event from above is
# rolled, this is where the information comes from. Whether a global
# or local event, the structure is the same.
industrial disaster:
   # A simple name for your event. This must be unique for this
   # type of event.
  syrup spill:

    # A title for the event.
    title: A maple syrup spill

    # A short description of your event to help flesh it out.
    # I recommend using the pipe and formatting the entries. This
    # will help readability when the script prints it out.
    description: |
      A holding container for maple syrup has broken, spilling syrup into the streets!
      The Player Character should try to eat as much as they can!

    # A list of necessary people for this event to happen. These
    # will be rolled automatically. The list can be empty, but
    # the key should still be included.
    needed:
      - villain

    # A list of optional people that you might want to have around,
    # but aren't strictly necessary for the event to play out. As above,
    # they will be rolled automatically and the list can be empty, but
    # not missing.
    optional:
      - ally

# A list of different villains that might have caused trouble.
# This is only to provide a little background on the character.
# Each of these should correspond to a listing in the npcs
# list above.
villain:
  - a Rival
  - an Ally now turned Rival

# For each name origin above, you'll need a list of names to
# pull from.
english:
  male:
    - Adam
    - Albert
    - Alfred
    - Allan
  female:
    - Abigail
    - Anne
    - Beatrice
    - Blanche
  surname:
    - Barker
    - Brown
    - Butler
    - Carter
```

## To do

- [ ] finish writing NPC selection
