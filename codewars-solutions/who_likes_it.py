"""
Implement the function which takes an array containing the names of people that like an item. 
It must return the display text as shown in the examples:
[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
"""

def likes(names):
  if len(names) == 0:
    return "no one likes this"
  elif len(names) == 1:
    return f'{names[0]} likes this' 
  elif len(names) == 2:
    return f'{names[0]} and {names[1]} like this' 
  elif len(names) == 3:
    return f'{names[0]}, {names[1]} and {names[2]} like this' 
  elif len(names) > 3:
    nombres=len(names)-2
    return f'{names[0]}, {names[1]} and {nombres} others like this' 
