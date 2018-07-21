# rpgrandom
requires a table.yml file in the same directory as the script.
the YAML file should have the following format

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

## To do:
 - [ ] finish writing NPC selection

## License
Copyright (c) 2018 serenewaffles

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.