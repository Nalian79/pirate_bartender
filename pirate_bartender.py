import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit o' sweetness wit yer poison?",
    "fruity": "Are ye one fer a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "splash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

adj = ["Fluffy", "Salty", "Bitter", "Stale", "Prickly", "Sour", "Sweet"]
noun = ["Whale-tail", "Shark-Snout", "Sea-Dog", "kraken", "One-eyed Parrot", "Swabbie"]

def style_o_drink():
    """This function gathers the users drink preferences for a dict.

    Use raw_input() to create a dictionary with boolean values for their
    responses.
    """
    answers = {}
    for key in questions.iterkeys():
        answers[key] = raw_input(questions[key] + " Type Y or N: ").upper()
        if answers[key] == "Y":
            answers[key] = True
        else:
            answers[key] = False
    return answers

def make_drink(answers):
    """Create a drink randomly based on the users choices."

    This function takes the answers from the style_o_drink function
    and then creates a drink out of the ingrediants list, based on those
    user inputs.
    """
    drink = []
    for key, value in answers.iteritems():
        if answers[key]:
            item = random.choice(ingredients[key])
            drink.append(item)
            print "Added a " + item + " to yer drink."
        else:
            pass
    return drink

def drink_name():
    """Create a drink name randomly out of the noun and adj lists. """

    thing = random.choice(noun)
    desc = random.choice(adj)
    print "Gar, here be yer " + desc + " " + thing

def main():
    """Put the drinks and naming all together"""

    while True:

        want_drink = raw_input("Do ye want a drink? (Y/N) ").upper()
        if want_drink == 'Y':
            # Create the user-generated answer dictionary
            answers = style_o_drink()
            # Use the dictionary to make a random drink
            drink = make_drink(answers)
            # Give the drink a random name
            drink_name()
        else:
            print "Next time, landlubber."
            break


if __name__ == '__main__':
    main()

