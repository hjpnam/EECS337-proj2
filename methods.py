from nltk import pos_tag, word_tokenize, tokenize

PRIMARY_METHODS_LIST = ["bake", "boil", "broil", "cook", "grill", "poach", "sautee", "stir-fry"]
OTHER_METHODS_LIST = ["chop", "crush", "cut", "dice", "drain", "grate", "grease", "melt", "mince", "mix", "pour", "preheat", "reduce", "season", "shake", "slice", "spread", "sprinkle", "squeeze", "stir"]

def get_method(step):
    # NOT ACCURATE - adds pronoun to the beginning of each sentence
    sentences = tokenize.sent_tokenize(direction)
    pronoun_sentences = []
    text = ""
    for sentence in sentences:
        pronoun_sentences.append("she " + sentence.lower())

    a_text = []
    for sentence in pronoun_sentences:
        a_text.append(word_tokenize(sentence))

    for item in a_text:
        print pos_tag(item)
    return pronoun_sentences

def get_primary_methods(step):
    primary_methods = []
    for method in PRIMARY_METHODS_LIST:
        if method in step:
            primary_methods.append(method)
        elif method + "ing" in step:
            method = method[:-3]
            primary_methods.append(method)
        elif method + "ed" in step:
            method = method[:-2]
            primary_methods.append(method)
    return set(primary_methods)

def get_other_methods(step):
    other_methods = []
    for method in OTHER_METHODS_LIST:
        if method in step:
            other_methods.append(method)
        elif method + "ing" in step:
            method = method[:-3]
            other_methods.append(method)
        elif method + "ed" in step:
            method = method[:-2]
            other_methods.append(method)
    return set(other_methods)

sentence = "In a skillet, cook sausage, onion and garlic until pork is no longer pink and onion is tender; drain. Add marinara sauce and oregano; simmer for 5 minutes. In a bowl, combine ricotta cheese, egg, 1/4 cup Parmesan and spinach. In a greased 13-in. x 9-in. x 2-in. baking dish, spread 1 cup meat sauce. Arrange 3 noodles over sauce. Spread one-fourth of the ricotta cheese mixture over the noodles, top with 1 cup of meat sauce. Sprinkle with 1/2 cup mozzarella cheese. Repeat process 3 times. Top with remaining Parmesan cheese. Bake, uncovered, at 350 degrees F for 40 to 45 minutes. Let stand for 10 minutes before cutting. Serve."

print get_primary_methods(sentence.lower())
print get_other_methods(sentence.lower())
