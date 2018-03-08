import nltk
from nltk import pos_tag, word_tokenize, tokenize
from Vocabulary import *

def get_primary_methods(steps):
    primary_methods_found = []
    for step in steps:
        for method in primary_methods:
            if method in step.lower():
                primary_methods_found.append(method)
            elif method + "ing" in step.lower():
                method = method[:-3]
                primary_methods_found.append(method)
            elif method + "ed" in step.lower():
                method = method[:-2]
                primary_methods_found.append(method)
            elif method + "d" in step.lower():
                method = method[:-1]
                primary_methods_found.append(method)
            elif method + "s" in step.lower():
                method = method[:-1]
                primary_methods_found.append(method)
    return set(primary_methods_found)

def get_other_methods(steps):
    other_methods_found = []
    for step in steps:
        for method in other_methods:
            if method in step.lower():
                other_methods_found.append(method)
            elif method + "ing" in step.lower():
                method = method[:-3]
                other_methods_found.append(method)
            elif method + "ed" in step.lower():
                method = method[:-2]
                other_methods_found.append(method)
            elif method + "d" in step.lower():
                method = method[:-1]
                primary_methods_found.append(method)
            elif method + "s" in step.lower():
                method = method[:-1]
                primary_methods_found.append(method)
    return set(other_methods_found)

example = [u'Bring a large pot of lightly salted water to a boil; add penne and cook, stirring occasionally, until tender yet firm to the bite, about 11 minutes. Drain.', u'Pour artichoke marinade into a large nonstick skillet over medium heat. Add chicken; cook and stir until white, about 3 minutes. Add mushrooms; cook and stir until chicken is no longer pink in the center, 4 to 6 minutes. Stir in artichokes.', u'Mix chicken broth, white wine, and cornstarch together in a bowl until cornstarch is dissolved. Pour into the skillet slowly, stirring constantly until sauce comes to a boil. Reduce heat and simmer until thickened, about 5 minutes.', u'Toss chicken mixture with penne in a large bowl. Season with salt and pepper.', u'']

print "primary methods", get_primary_methods(example)
print "other methods", get_other_methods(example)
