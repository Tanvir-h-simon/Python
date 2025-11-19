# frozenset is an immutable version of a set.
# Like sets, it contains unique, unordered, unchangeable elements.
# Unlike sets, elements cannot be added or removed from a frozenset.
# Being immutable means you cannot add or remove elements. However, frozensets support all non-mutating operations of sets.
frozen_set = frozenset({"apple", "banana", "cherry"})
print(frozen_set)
print(type(frozen_set))

frozen_set = frozenset({1, 2, 3, 4, 5})
print(frozen_set)

# 2D set
frozen_set = ({1, 2, 3},
              {4, 5, 6},
              {7, 8, 9})
print(frozen_set)

# Copy set
set1 = frozenset({1, 2, 3, 4, 5})
set2 = set1.copy()
print(set1)