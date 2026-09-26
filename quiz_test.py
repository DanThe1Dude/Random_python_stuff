import random


dict = {"a": "b", "c": "d", "e" : "f"}
keys = list(dict.keys())
shuffled_keys = keys.copy()
random.shuffle(shuffled_keys)
print(f"dicts: {dict}\nkeys: {keys}\nShuffled keys {shuffled_keys}")
