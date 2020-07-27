import random

color = ['red','blue','green','silver','orange','aqua','a color that has no name','the inky dark black of midnight']
food = ['meatballs','banana','cake','bacon','pizza','guac','salsa','soup']
weather = ['cloudy with a chance of meatballs','stormy','rainy','cloudy','volcano-y']
character = ['lupin','harry potter','hermonie','ron','snape','hagrid','he who shall not be named']
drink = ['butter beer','fire whisky','old cauldron slime','fizzy pop','pumpkin juice','water','fanta']
magical_animal = ['unicorn','dragon','acromantula','hippogriff','centaur','phoenix']
pet = ['owl','cat','blobfish']

print(f'One day, I asked my mother for a {random.choice(color)} {random.choice(pet)}, but instead, she accidently got me a {random.choice(color)} {random.choice(magical_animal)}')
print(f'You might think this was a good thing, but my pet wanted to eat {random.randint(2,500)} servings of {random.choice(color)} {random.choice(food)} every morning')
print(f'I called {random.choice(character)} for advice and they said to go out when it was {random.choice(weather)} and the sky was {random.choice(color)} and let my pet go')
print(f'The strange thing is that it started raining {random.choice(color)} {random.choice(drink)} so I may have used the wrong spell, but my pet turned into a {random.choice(color)} {random.choice(pet)}')
print(f'Next time I am going to go to the petstore just to be on the safe side, and bring some {random.choice(color)} {random.choice(food)} with me just to be sure')
print(f'')