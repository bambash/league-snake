import json
import logging
import time

# Champions class


class Champions():
    def __init__(self):
        # switch to using remote json from datadragon.
        with open("champion.json") as f:
            d = json.load(f)
        self.data = d['data']
        self.ids = [c for c in self.data.keys()]

    # retrun json object of champion data
    def toJSON(self):
        return json.dumps(self, default=lambda o: self.data,
                          sort_keys=True, indent=4)

    # return a list of all champions as Champion class
    def toList(self):
        return [Champion(self.data[c]) for c in self.data.keys()]

    def listByChampionTag(self, tag: str):
        # format tag input
        tag = tag.lower()
        tag = tag.capitalize()
        a = []
        for c in self.toList():
            if tag in c.data['tags']:
                a.append(c)
        return a

    # return a Champion based on "name" input

    def lookupByName(self, name: str):
        try:
            return Champion(self.data[name])
        except KeyError:
            logging.exception(f"Unable to find champion {name}")

    # retrun a Champion based on "number" input
    def lookupByNumber(self, number: int):
        try:
            for key in self.data:
                if str(number) == self.data[key]['key']:
                    champion = Champion(self.data[key])
                    break
            if not champion:
                raise(f"Unable to find champion number {number}")
            else:
                return champion
        except Exception as e:
            print(e)


# Champion class
class Champion():
    def __init__(self, data):
        # set some default instance attributes
        # do something better
        self.name = data['name']
        self.id = data['key']
        self.title = data['title']
        self.data = data
        self.stats = data['stats']

    # return a json object of champion data
    def toJSON(self):
        return json.dumps(self, default=lambda o: self.data,
                          sort_keys=True, indent=4)


# input champions[], stat; selection sort ascending
def insertion_sort_by_stat(champions, stat):
    length = range(1, len(champions))

    for i in length:
        sort_me = champions[i].stats[stat]
        while champions[i-1].stats[stat] > sort_me and i > 0:
            champions[i], champions[i-1] = champions[i-1], champions[i]
            i = i - 1

    return champions


# input champions[], stat; quick sort ascending
def quick_sort_by_stat(champions, stat):
    length = len(champions)
    if length <= 1:
        return champions
    else:
        pivot = champions.pop()

    lower = []
    higher = []
    for i in champions:
        if i.stats[stat] < pivot.stats[stat]:
            lower.append(i)
        else:
            higher.append(i)

    return quick_sort_by_stat(lower, stat) + [pivot] + quick_sort_by_stat(higher, stat)


# input champions[], stat; selection sort ascending
def selection_sort_by_stat(champions, stat):
    length = range(0, len(champions) - 1)
    for i in length:
        min_value = champions[i].stats[stat]
        for j in range(i+1, len(champions)):
            if champions[j].stats[stat] < min_value:
                min_value = champions[j].stats[stat]
                champions[j], champions[i] = champions[i], champions[j]

    return champions

# input champions[], stat; bubble sort ascending


def bubble_sort_by_stat(champions, stat):
    length = len(champions) - 1
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(0, length):
            if champions[i].stats[stat] > champions[i+1].stats[stat]:
                champions[i], champions[i+1] = champions[i+1], champions[i]
                is_sorted = False
    return champions


champs = Champions()
mage_health = bubble_sort_by_stat(champs.listByChampionTag("tank"), "hp")
[print(c.name, c.stats['hp']) for c in mage_health]
