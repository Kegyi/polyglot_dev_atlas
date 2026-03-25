# 17.07. Baby Names

## Description

Every year, the government releases a list of the 10000 most common baby names and their
frequencies. The only problem with this approach is that some names have multiple
spellings. For example, "John" and "Jon" are essentially the same name but would be
listed separately in the list. Given two lists, one of names/frequencies and one of pairs
of equivalent names, write an algorithm to print a new list of the true frequency of each
name. Note that if John and Jon are synonyms, and Jon and Johnny are synonyms, then John,
Jon, and Johnny are all synonyms. (It is both transitive and symmetric.) In the final
list, choose the name that are lexicographically smallest as the "real" name.

**Example:**

```
Input:
  names = ["John(15)","Jon(12)","Chris(13)","Kris(4)","Christopher(19)"]
  synonyms = ["(Jon,John)","(John,Johnny)","(Chris,Kris)","(Chris,Christopher)"]
Output: ["Chris(36)","John(27)"]
```

## Implementations

- [C++](cpp.cpp)
- [Python](python.py)
- [Go](go.go)
- [TypeScript](typescript.ts)
- [Scala](scala.scala)

## Expected Output

```
Chris(36) John(27)
```
