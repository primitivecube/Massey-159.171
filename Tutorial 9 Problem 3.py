# By Brett McDonald
# SID: 10158931
# Tutorial 9
# Problem 3: Maintaining search statistics

foundCount = 0
searchCount = 0
names = [ "Mary", "Liz", "Miles", "Bob", "Fred" ]
numbers = [ 4, 17, 19]

def find (item):
  global foundCount
  global searchCount
  global notFoundCount # need to confirm that this 5th global variable is necessary; the instructions said 'using four global variables'
  searchCount += 1
  searchNumbers = True
  notFound = True
  for name in names:
    if item == name:
      foundCount += 1
      searchNumbers = False
      notFound = False
      print("Found in Names")
  if searchNumbers:
    for number in numbers:
      if item == number:
        foundCount += 1
        notFound = False
        print("Found in Numbers")
  if notFound:
    print("Not found")

def results():
  print("Total searches: {:>2}".format(foundCount))
  print("Total matches : {:>2}".format(searchCount))
  print("Total not found: {}".format(searchCount - foundCount))

find("mary")
find("Mary")
find(0)
find(19)
results()

# Results
# Not found
# Found in Names
# Not found
# Found in Numbers
# Total searches:  2
# Total matches :  4
# Total not found: 2
