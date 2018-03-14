# Database file for vocabulary needed throughout the project.

measurements = [
    'cup', 'cups',
    'gram', 'grams',
    'kilogram', 'kilograms',
    'liter', 'liters',
    'pound', 'pounds',
    'milliliter', 'milliliters',
    'ounce', 'ounces',
    'pint', 'pints',
    'teaspoon', 'teaspoons',
    'tablespoon', 'tablespoons',
    'pinch', 'pinches',
    'fillet', 'fillets',
    'clove', 'cloves',
    'can', 'cans',
    'loaf', 'loaves',
    'slice', 'slices',
    'handful', 'handfuls',
    'stalk', 'stalks',
    'head', 'heads',
    'drop', 'drops',
    'can', 'cans',
    'quart', 'quarts',
    'gallon', 'gallons',
    'package', 'packages',
    'sprig', 'sprigs',
    'dash', 'dashes',
    'envelope', 'envelopes',
    'piece', 'pieces'
]

vegetarian = ['seitan',
    'lentil',
    'tofu',
    'mushroom'
]

vegetarian_attribute = {
    'seitan': {'servingSize': 0.5, 'measurement': 'cup'},
    'lentil': {'servingSize': 0.5, 'measurement': 'cup'},
    'tofu': {'servingSize': 150, 'measurement': 'gram'},
    'mushroom': {'servingSize': 90, 'measurement': 'gram'}
}

meat_priority = {
    'chicken broth': 'mushroom broth',
    'beef broth': 'mushroom broth',
    'chicken stock': 'mushroom broth',
    'bone broth': 'mushroom broth',
    'turkey stock': 'mushroom broth',
    'beef stock': 'mushroom broth',
}

meat_trash = [
	'spareribs',
	'ribs',
	'chop',
	'rib',
	'chops',
	'loin',
	'sirloin',
	'steak',
	'meat',
	'meatloaf'
]

meat = {
	'spare ribs': 'seitan',
	'spare rib': 'seitan',
	'spareribs': 'seitan',
	'sparerib': 'seitan',
	'ribs': 'seitan',
	'rib': 'seitan',
    'bacon': 'tofu',
    'bear': 'tofu',
    'beef': 'tofu',
    'buffalo': 'tofu',
    'bison': 'tofu',
    'calf': 'tofu',
    'caribou': 'tofu',
	'chicken meat': 'mushroom',
	'chicken breast': 'mushroom',
	'chicken breasts': 'mushroom',
	'chicken wing': 'mushroom',
	'chicken wings': 'mushroom',
    'chicken': 'mushroom',
    'goat': 'tofu',
    'ham': 'mushroom',
    'horse': 'tofu',
    'kangaroo': 'tofu',
	'lamb chops': 'jackfruit',
	'lamb chop': 'jackfruit',
	'lamb rib': 'jackfruit',
    'lamb': 'jackfruit',
    'moose': 'tofu',
    'mutton': 'tofu',
    'opposum': 'tofu',
	'pork loin': 'jackfruit',
    'pork': 'jackfruit',
    'rabbit': 'tofu',
    'snake': 'mushroom',
    'squirrel': 'seitan',
		't-bone steak': 'tofu',
    'steak': 'tofu',
    'sweetbreads': 'mushroom',
    'tripe': 'tofu',
	'andouille sausage': 'lentils',
	'andouille sausages': 'lentils',
	'sausage': 'lentil',
	'turkey sausage': 'lentil',
    'turkey': 'tofu',
    'turtle': 'seitan',
    'veal': 'tofu',
    'venison': 'tofu'
}

fish = [
    'abalone',
    'alaska pollock',
    'albacore tuna',
    'american lobster',
    'american shad',
    'anchovy',
    'arctic char',
    'atlantic mackerel',
    'atlantic ocean perch',
    'atlantic salmon',
    'barracuda',
    'barramundi',
    'basa',
    'bay scallop',
    'black sea bass',
    'black tiger shrimp',
    'blue crab',
    'blue marlin',
    'bluefin tuna',
    'bream',
    'carp',
    'catfish',
    'chilean sea bass',
    'chinese white shrimp',
    'chinook salmon',
    'chum salmon',
    'cobia',
    'cockle',
    'cod',
    'coho salmon',
    'conch',
    'crab',
    'crayfish',
    'croaker',
    'cusk',
    'cuttlefish',
    'dogfish',
    'dory',
    'dover sole',
    'drum',
    'dungeness crab',
    'eastern oyster',
    'eel', 'escolar',
    'european oyster',
    'european sea bass',
    'flounder',
    'freshwater shrimp',
    'geoduck clam',
    'greenshell mussel',
    'grouper',
    'gulf shrimp',
    'haddock',
    'hake',
    'halibut',
    'hardshell clam',
    'herring',
    'hoki',
    'hybrid striped bass',
    'jonah crab',
    'king crab',
    'kingklip',
    'lake victoria perch',
    'lake whitefish',
    'lingcod',
    'lobster',
    'mackrel',
    'mahimahi',
    'mako shark',
    'moi',
    'monkfish',
    'mullet',
    'octopus',
    'opah',
    'orange roughy',
    'pacific oyster',
    'pacific white shrimp',
    'peekytoe crab',
    'pink salmon',
    'pink shrimp',
    'pollock',
    'pompano',
    'rainbow trout',
    'rock shrimp',
    'rockfish',
    'sablefish',
    'salmon',
    'sardine',
    'scup',
    'sea scallop',
    'sea urchin',
    'shrimp',
    'skate',
    'smelt',
    'snapper',
    'snow crab',
    'sockeye salmon',
    'spanner crab',
    'spiny lobster',
    'squat lobster',
    'squid',
    'stone crab',
    'sturgeon',
    'surf clam',
    'swordfish',
    'tilapia',
    'tilefish',
    'trout',
    'tuna',
    'turbot',
    'wahoo',
    'walleye',
    'wolffish',
    'yellow perch',
    'yellowfin tuna',
    'yellowtail'
]

descriptors = [
    'skinless',
    'boneless',
    'dried',
    'shredded',
    'extra-virgin',
    'fresh', 'freshly',
    'frozen',
    'canned',
    'cold',
    'small',
    'medium',
    'large',
    'bone-in',
    'whole'
]

primary_methods = [
    'bake',
    'boil',
    'braise',
    'broil',
    'cook',
    'deep-fry',
    'fry',
    'grill',
    'pan-fry',
    'poach',
    'pressure-cook',
    'roast',
    'saute',
    'sautee',
    'sear',
    'smoke',
    'steam',
    'stir-fry'
]

other_methods = [
    'add',
    'beat',
    'caramelize',
    'chop',
    'coat',
    'crush',
    'cut',
    'debone',
    'dice',
    'drain',
    'drizzle',
    'freeze',
    'garnish',
    'glaze',
    'grate',
    'grease',
    'grind',
    'marinate',
    'mash',
    'melt',
    'mince',
    'mix',
    'peel',
    'pour',
    'preheat',
    'pre-heat',
    'puree',
    'reduce',
    'refrigerate',
    'reheat',
    'rinse',
    'rub',
    'scramble',
    'season',
    'shake',
    'sift',
    'simmer',
    'slice',
    'spread',
    'sprinkle',
    'squeeze',
    'steep',
    'stir',
    'strain',
    'stuff',
    'sweeten',
    'tenderize',
    'thaw',
    'toss',
    'wash',
    'whip',
    'whisk'
]

healthy_substitutes = {
# ingredients
    'rice':'quinoa',
    'couscous':'quinoa',
    'flour tortilla':'corn tortilla',
    'stevia':'sugar',
    'bread': 'whole wheat bread',
    'soda':'tonic water',
    'french fries':'sweet potato fries',
    'potato chips':'kale chips',
    'sour cream':'greek yogurt',
    'mayonaise':'mustard',
    'croutons':'nuts',
    'chocolate chips':'cacao nibs',
    'peanut butter':'almond butter',
    'milk':'almond milk',
    'flour':'whole-wheat flour',
    'beef':'turkey',
    'iceberg lettuce':'dark leafy greens',
    'ice cream':'frozen fruit',
    'cream cheese':'low-fat cottage cheese',
    'cornstarch':'potato starch',
    'butter':'coconut oil',
    'half-and-half':'skim milk',
# methods
    'boil':'steam',
    'deep-fry':'pan-fry'
}

indian_substitutes = {
    'marinara sauce':'curry sauce',
    'pesto':'curry',
    'parmesan cheese':'paneer',
    'mozzerella':'paneer',
    'cheddar':'paneer',
    'provolone':'paneer',
    'cheese':'paneer',
    'penne pasta':'rice',
    'penne':'rice',
    'macaroni':'rice',
    'pasta':'rice',
    'beef':'lamb'
}

italian_substitutes = {
    'rice':'pasta',
    'quinoa':'pasta',
    'cheddar':'mozzarella',
    'cream cheese':'mascarpone',
    'salsa':'marinara sauce',
    'ice cream':'gelato',
    'peanut oil':'olive oil',
    'sesame oil':'olive oil',
    'beef':'italian sausage',
    'baked beans':'cannellini beans'
}
