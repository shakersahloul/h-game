def main_menu():
    #  Print the introduction and available player commands
    print("Oh joy...another mortal. Well, mortal, if you would like to return to your own world feel free to "
          "wander the Master's garden in search of an exit.")
    print("There are six unique items you will need to collect in order to return home. Oh! And mind the Mind Flayers.")
    print("They will take your sanity as surely as staying in this garden would. Good luck...")
    print()
    print("Move Commands: North, South, West, East")
    print("Add to Inventory: get 'Item'")
    print("-----------------------------------------------------------------------------------------------------")


def you_died():
    print('You reach the peaceful shores of the drowned lake and suddenly you'
          'feel an alien presence in your mind... It is too late to run, you are dead.')

def main():
    main_menu()
    # Create a dictionary to house the rooms and items
    rooms = {
        'Garden of Madness': {'name': 'Garden of Madness', 'South': 'Screaming Tombs', 'North': 'Bone Orchard',
                              'East': 'Dream Cells', 'West': 'Wraith Point', 'item': 'nothing'},
        'Screaming Tombs': {'name': 'Screaming Tombs', 'North': 'Garden of Madness', 'East': 'Ghost Raven Grotto',
                            'item': 'a Wooden Spoon'},
        'Ghost Raven Grotto': {'name': 'Ghost Raven Grotto', 'West': 'Screaming Tombs', 'item': 'Moldy Cheese'},
        'Bone Orchard': {'name': 'Bone Orchard', 'South': 'Garden of Madness', 'East': 'Cheerful Mausoleum', 'item':
                         'a Hand'},
        'Cheerful Mausoleum': {'name': 'Cheerful Mausoleum', 'West': 'Bone Orchard', 'item': 'a Book of Jokes'},
        'Dream Cells': {'name': 'Dream Cells', 'West': 'Garden of Madness', 'North': 'Soul Vineyard', 'item':
                        'a Pretty Crystal'},
        'Soul Vineyard': {'name': 'Soul Vineyard', 'South': 'Dream Cells', 'item': 'a Squirrel'},
        'Wraith Point': {'name': 'Wraith Point', 'East': 'Garden of Madness', 'North': 'Drowned Lake',
                         'item': 'nothing'},
        'Drowned Lake': {'name': 'Drowned Lake', 'item': 'the Mind Flayer!!'}  # Villain!!
    }

    # Establish how players current location will be called
    current_loc = rooms['Garden of Madness']

    # Establish the current commands available to the player
    commands = ['North', 'South', 'West', 'East', 'Item']

    # Create a blank list for the inventory
    inventory = []


    # Begin the game
    while True:
        print('You are in the {}.'.format(current_loc['name'], ))  # Print the player's current location
        print('This room contains {}.'.format(current_loc['item'], ))  # Print the item in the locations
        print('Your Inventory: {}'.format(inventory, ))  # Print the player's inventory

        command = input('\nWhat would you like to do?').strip()  # Get player command input
        if command in commands:

            if command in current_loc:
                current_loc = rooms[current_loc[command]]
                # FIXME game needs to call the you_died function and end the game in 'Drowned Lake'
            else:
                # Prompt user to choose a valid direction
                print('You run headlong into a wall and take a nasty bump on your head.'
                      'Please try a different direction.')

        elif command.lower() in 'quit':  # quit command valid for testing only
            print('You embrace the insanity within and skip gleefully into madness.')
            break
        else:
            # Print statement when invalid command is given
            print('The madness of this place must be getting to you. Please give a valid command.')
    print()


main()
