names = [
    "Adam",
    [
        "Bob",
        [
            "Chet",
            "Cat",
        ],
        "Barb",
        "Bert"
    ],
    "Alex",
    [
        "Bea",
        "Bill"
    ],
    "Ann"
]

print(len(names))
for index, item in enumerate(names):
    print(index, item)

# To count all the names in the list names
# we have to go through some steps:
# 1- Walk through the list, examining each item in turn.
# 2- If you find a leaf element, then add it to the accumulated count.
# 3- If you encounter a sublist, then do the following:
#    Drop down into that sublist and similarly walk through it.
#    Once you’ve exhausted the sublist, go back up, add the elements from the sublist to the accumulated count, and resume the walk through the parent list where you left off.


# to know if a given list item is leaf item or not
# we can use isinstance()
print(isinstance(names[0], list))
# names[0] is not a leaf item of names
print(isinstance(names[1], list))
# names[1] is a leaf item of names


def count_leaf_items(items_list):
    """Recursively counts and returns the
       number of leaf items in a (potentially
       nested) list.
    """
    count = 0
    for item in items_list:
        if isinstance(item, list):
            count += count_leaf_items(item)
        else:
            count += 1
    return count