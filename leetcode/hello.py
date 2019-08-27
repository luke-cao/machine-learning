import collections


def find_anagrams(dictionary):
    sorted_string_to_anagrams = collections.defaultdict(list)
    for s in dictionary:
        sorted_string_to_anagrams[''.join(sorted(s))].append(s)
    return [group for group in sorted_string_to_anagrams.values() if len(group) >= 2]


inputs = ["debitcard", "elyis", "silent", "badcredit", "lives", "fteedom", "listen", "levis", "money"]
print(inputs)
print(find_anagrams(inputs))

print(hash('hello'))