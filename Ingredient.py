import nltk
from nltk.tokenize import word_tokenize

measurements = ['cup', 'cups', 'gram', 'grams', 'kilogram', 'kilograms', 'liter', 'liters', 'pound', 'pounds', 'milliliter', 'milliliters', 'ounce', 'ounces', 'pint', 'pints', 'teaspoon', 'teaspoons', 'tablespoon', 'teaspoons', 'pinch', 'fillet', 'fillets', 'clove', 'cloves']
descriptors = ['skinless', 'boneless', 'dried', 'shredded', 'extra-virgin', 'freshly']

class Ingredient:

    def __init__(self, string):

        self.data = {
            'name': '',
            'quantity': '',
            'measurement': 'none',
            'descriptor': [],
            'preparation': 'none'
        }

        tokenized = word_tokenize(string)
        tagged = nltk.pos_tag(tokenized)
        next = 0

        if (tagged[0][1] == 'CD'):
            if (tagged[1][1] == 'CD'):
                self.data['quantity'] = tagged[0][0] + ' ' + tagged[1][0]
                next = 2
            else:
                self.data['quantity'] = tagged[0][0]
                next = 1

        parenString = ''
        if (tagged[next][0] == '('):
            parenString += '('
            next += 1
            while (tagged[next][0] != ')'):
                parenString += tagged[next][0] + ' '
                next += 1
            parenString = parenString[:-1]
            parenString += ')'
            next += 1

        if (tagged[next][0].lower() in measurements):
            self.data['measurement'] = tagged[next][0]
            next += 1

        nameList = []
        descriptorList = []
        for i in range(next, len(tagged)):
            if (tagged[i][1] == 'JJ' or tagged[i][0].lower() in descriptors):
                descriptorList.append(tagged[i][0])
                next += 1
                continue
            if (tagged[i][0] == ',' and not (tagged[i-1][1] == 'JJ' or tagged[i-1][0].lower() in descriptors)):
                break
            nameList.append(tagged[i][0])
            next += 1

        self.data['name'] = parenString + " ".join(nameList)
        self.data['descriptor'] = descriptorList

        if (next != len(tagged) and tagged[next+1][0] != 'or'):
            self.data['preparation'] = " ".join(tokenized[next + 1:])

    def getData(self):
        return self.data

    def getName(self):
        return self.data['name']

    def getQuantity(self):
        return self.data['quantity']

    def getMeasurement(self):
        return self.data['measurement']

    def getDescriptor(self, string = False):
        if (string):
            return ", ".join(self.data['descriptor'])
        else:
            return self.data['descriptor']

    def getPrepation(self):
        return self.data['preparation']