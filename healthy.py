# transformation to healthy recipe

healthy_substitutes = {
# ingredients
    "rice":"quinoa",
    "couscous":"quinoa",
    "flour tortilla":"corn tortilla",
    "stevia":"sugar",
    "bread": "whole wheat bread",
    "soda":"tonic water",
    "french fries":"sweet potato fries",
    "potato chips":"kale chips",
    "sour cream":"greek yogurt",
    "mayonaise":"mustard",
    "croutons":"nuts",
    "chocolate chips": "cacao nibs",
    "peanut butter": "almond butter",
    "milk":"almond milk",
    "flour":"whole-wheat flour",
    "beef":"turkey",
    "iceberg lettuce":"dark leafy greens",
    "ice cream":"greek yogurt",
    "cream cheese":"low-fat cottage cheese",
# methods
    "boil":"steam",
    "deep-fry":"pan-fry"
}

def to_healthy(steps):
    # options: gluten-free, low-sodium
    for i, step in enumerate(steps):
        for ingredient in healthy_substitutes.keys():
            if ingredient in step:
                step = switch_ingredient(step, ingredient)
                steps[i] = step
    return steps

def switch_ingredient(step, ingredient):
    substitute = healthy_substitutes[ingredient]
    return step.replace(ingredient, substitute)

steps = ["Pour beef with soy sauce marinade into the hot skillet; cook and stir until browned completely, about 5 minutes. Return vegetable mixture to the skillet; bring to a simmer. Cook and stir until completely hot, about 2 minutes.", "make french fries and boil peanut butter"]

print to_healthy(steps)
