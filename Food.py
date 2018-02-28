import nltk
from nltk.tokenize import word_tokenize

fish = ['abalone', 'alaska pollock', 'albacore tuna', 'american lobster', 'american shad', 'anchovy', 'arctic char', 'atlantic mackerel', 'atlantic ocean perch', 'atlantic salmon', 'barracuda', 'barramundi', 'basa', 'bay scallop', 'black sea bass', 'black tiger shrimp', 'blue crab', 'blue marlin', 'bluefin tuna', 'bream', 'carp', 'catfish', 'chilean sea bass', 'chinese white shrimp', 'chinook salmon', 'chum salmon', 'cobia', 'cockle', 'cod', 'coho salmon', 'conch', 'crab', 'crayfish', 'croaker', 'cusk', 'cuttlefish', 'dogfish', 'dory', 'dover sole', 'drum', 'dungeness crab', 'eastern oyster', 'eel', 'escolar', 'european oyster', 'european sea bass', 'flounder', 'freshwater shrimp', 'geoduck clam', 'greenshell mussel', 'grouper', 'gulf shrimp', 'haddock', 'hake', 'halibut', 'hardshell clam', 'herring', 'hoki', 'hybrid striped bass', 'jonah crab', 'king crab', 'kingklip', 'lake victoria perch', 'lake whitefish', 'lingcod', 'lobster', 'mackrel', 'mahimahi', 'mako shark', 'moi', 'monkfish', 'mullet', 'octopus', 'opah', 'orange roughy', 'pacific oyster', 'pacific white shrimp', 'peekytoe crab', 'pink salmon', 'pink shrimp', 'pollock', 'pompano', 'rainbow trout', 'rock shrimp', 'rockfish', 'sablefish', 'salmon', 'sardine', 'scup', 'sea scallop', 'sea urchin', 'shrimp', 'skate', 'smelt', 'snapper', 'snow crab', 'sockeye salmon', 'spanner crab', 'spiny lobster', 'squat lobster', 'squid', 'stone crab', 'sturgeon', 'surf clam', 'swordfish', 'tilapia', 'tilefish', 'trout', 'tuna', 'turbot', 'wahoo', 'walleye', 'wolffish', 'yellow perch', 'yellowfin tuna', 'yellowtail']

meat = ['bacon', 'beef', 'beef heart', 'beef liver', 'beef tongue', 'buffalo', 'bison', 'calf liver', 'caribou', 'chicken', 'chicken breast', 'chicken leg', 'chicken thigh', 'goat', 'ham', 'horse', 'kangaroo', 'lamb', 'moose', 'mutton', 'opposum', 'pork', 'rabbit', 'snake', 'squirrel', 'sweetbreads', 'tripe', 'turtle', 'veal', 'venison']

class Food:

    def __init__(self, string):

        self.data = {
            'name': '',
            'quantity': '',
            'measurement': '',
            'descriptor': '',
            'preparation': ''
        }
        self.meat = False

        tokenized = word_tokenize(string)
        tagged = nltk.pos_tag(tokenized)

        for i in range(0, len(tagged)):
            tag = tagged[i]

    def isMeat(self):
        return False
