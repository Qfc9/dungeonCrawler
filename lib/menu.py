# store custom menu items DONE
# those items should be executable DONE
# items should be selectable DONE
# should be able to display items DONE
class Menu():
    """ Displays a menu and runs the selected function.
         - There is no limit to the amount of menu items.
         - The selected function needs to be specified when adding a menu item.
         - The order in which the menu items are displayed is the same as the order in which they were added.
         - The menu item name and function are saved in a list.
         - The index of the selected menu item is translated to the index of the list it is stored in.
         - The selected function is run by indexing into the list with the translated index.

         Attributes:
         menuItems: The list that contains the menu items.
         - The menu items are stored in sublists, containing the text and the function.
    """
    def __init__(self):
        """ Initialises an empty list to store the menu items. """
        self.menuItems = []

    def addMenuItem(self, text: str, function, param=None):
        """ Adds a `menu item to` the menuItems list.
            - The menu item's text and function need to be specified when calling this function.
            - The menu item is added to the menuItems list. """
        self.menuItems.append([text, function, param])

    def displayMenu(self):
        """ Displays the menu items in the menuItems list.
            - Each menu item is displayed with the menu index in front of it.
            - The menu index is used to select the menu item.
            - The menu index is equal to the index of the menu item in the menuItems list.
        """
        for idx, item in enumerate(self.menuItems):
            print("{}) {}".format(idx, item[0]))

    def runItem(self, menuIdx: str):
        """ Runs the selected function.
            - The menu index is translated to the index of the menu item in the menuItems list.
            - The function is run by indexing into the list with the translated index.
        """
        if menuIdx.isdigit():
            menuIdx = int(menuIdx)

            if menuIdx in range(0, len(self.menuItems)):

                if self.menuItems[menuIdx][2] is None:
                    return self.menuItems[menuIdx][1]()
                else:
                    return self.menuItems[menuIdx][1](self.menuItems[menuIdx][2])