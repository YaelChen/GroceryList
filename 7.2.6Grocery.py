
def grocery(ingredients):
    """the function helps organize the list of ingredients for grocery.
    :param ingredients: the ingredients needed.
    :type ingredients: str
    :return none:"""

    def count_ing(ing):
        return ingredients_list.count(ing)

    n = 0
    ingredients_list = ingredients.split(",")
    print(ingredients_list)
    while n != "9":
        n = input("""please choose an action number:
        1: Show ingredients
        2: Show number of ingredients
        3: Check if an ingredient is on the list
        4: Check how many times an ingredient is on the list
        5: Delete an ingredient from the list
        6: Add an ingredient to the list
        7: Show illegal ingredients
        8: Delete all double ingredient
        9: Exit
        
        Enter your choice: """)
        if n == "1":
            for i in ingredients_list:
                print(i)
        elif n == "2":
            print(len(ingredients_list))
        elif n == "3":
            ing = input("Please type an ingredient to check: ")
            if ing in ingredients_list:
                print(f"{ing} is in the list")
            else:
                print(f"{ing} is not in the list")
        elif n == "4":
            ing = input("Please type an ingredient to check: ")
            print(count_ing(ing))
        elif n == "5":
            ing = input("Please type one ingredient to delete: ")
            ingredients_list.remove(ing)
            print(f"{ing} has been deleted")
        elif n == "6":
            ing = input("Please type one ingredient to add: ")
            ingredients_list.append(ing)
            print(f"{ing} has been added")
        elif n == "7":
            for i in ingredients_list:
                if len(i) < 3 or not i.isalpha():
                    print(i)
        elif n == "8":
            for i in ingredients_list:
                if count_ing(i) > 1:
                    ingredients_list.remove(i)
            print("all doubles has been deleted")
        elif n == "9":
            print("Goodbye.")
        else:
            print("Error, try again.")


grocery("Milk,Cottage,Tomatoes")
