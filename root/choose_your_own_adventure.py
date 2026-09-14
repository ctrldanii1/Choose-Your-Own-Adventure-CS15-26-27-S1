user_choice = None

story = """You discover a mysterious door in an empty park.
A sign reads: ONE DOOR. EIGHT POSSIBILITIES.

A voice says:
"Every choice creates a different future."

A: Open the red door.
OR
B: Open the blue door.
"""

print(story)
user_choice = input().lower()

if user_choice == "a":
    story = """You enter a room filled with glowing objects.

A: Pick up a golden key.
OR
B: Pick up a silver compass.
"""
    print(story)
    user_choice = input().lower()

    if user_choice == "a":
        story = """The key unlocks a machine that can change your future.

A: Become a famous inventor.
OR
B: Help your family become successful.
"""
        print(story)
        user_choice = input().lower()

        if user_choice == "a":
            print("""You become a famous inventor.
Your inventions change the world.

THE END: THE FAMOUS INVENTOR""")
        else:
            print("""You use the machine to help your family.
Everyone lives a happier life.

THE END: THE FAMILY'S FUTURE""")

    else:
        story = """The compass leads you to a spaceship.

A: Travel to a new planet.
OR
B: Explore a mysterious space station.
"""
        print(story)
        user_choice = input().lower()

        if user_choice == "a":
            print("""You discover a new planet.
Scientists name it after you.

THE END: THE FIRST EXPLORER""")
        else:
            print("""You discover a library containing the history
of every possible future.

THE END: THE KEEPER OF KNOWLEDGE""")

else:
    story = """The blue door leads to a glowing forest.

A: Follow the flower-covered path.
OR
B: Follow the snowy path.
"""
    print(story)
    user_choice = input().lower()

    if user_choice == "a":
        story = """You discover a village where everyone has a special talent.

A: Become the village artist.
OR
B: Become the village inventor.
"""
        print(story)
        user_choice = input().lower()

        if user_choice == "a":
            print("""Your paintings bring happiness to the village.
You become known for your creativity.

THE END: THE CREATIVE DREAMER""")
        else:
            print("""Your inventions make the village famous.
You create a better future for everyone.

THE END: THE VILLAGE INVENTOR""")

    else:
        story = """You arrive at a frozen castle.

A: Ask to see the future.
OR
B: Ask to change the future.
"""
        print(story)
        user_choice = input().lower()

        if user_choice == "a":
            print("""You see thousands of possible futures.
You realize that knowing the future doesn't control it.

THE END: THE FUTURE WATCHER""")
        else:
            print("""You gain the power to change the future.
Every change creates another possibility.

THE END: THE FUTURE CHANGER""") 