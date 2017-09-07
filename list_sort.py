import operator


def handle_list_of_tuples(list):
    return sorted(sorted(list, key = lambda elem1: elem1[3:], reverse=True), key = lambda elem2: elem2[:2])

list = [
        ("Tom", "19", "167", "54"),
        ("Jony", "24", "180", "69"),
        ("Json", "21", "185", "75"),
        ("John", "27", "190", "87"),
        ("Jony", "24", "191", "98"),
        ]

print(handle_list_of_tuples(list))
