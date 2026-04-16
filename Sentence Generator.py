#import randint function from the random module using the import keyword.
from random import randint
#Give the list of names as static input store it in a variable.
gvn_names=["Me", "I", "You", "He", "She", "They", "We"]
#Give the list of verbs as static input store it in another variable.
gvn_verbs=["are", "is", "was", "were"]
#Give the list of nouns as static input store it in another variable.
gvn_nouns=["eating", "sleeping", "writing", "coding", "dancing", "reading"]
#Generate a random sentences using the randint () function with the given lists to name,
#verbs, nouns and print the result
print(gvn_names[randint(0,len(gvn_names)-1)]+" "+gvn_verbs[randint(0,len(gvn_verbs)-1)]+" "+gvn_nouns[randint(0,len(gvn_nouns)-1)])