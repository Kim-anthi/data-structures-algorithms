def locate_cards(cards, query):
  #create a variable position with value 0
  position = 0
  
  #loop
  while True:
    #check element at current position meets the query
    if cards[position] == query:
      #return the position and quit
      return position
    #increasing the potion
    position += 1
    
    #check the end of an array
    if position == len(cards):
      #return -1 if no number found
      return -1
    
tests = [
    {
        'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 7},
        'expected': 3
    },
    {
        'input': {'cards': [5, 4, 3, 2, 1], 'query': 2},
        'expected': 3
    },
    {
        'input': {'cards': [9, 7, 5], 'query': 4},
        'expected': -1
    }
]


for i, test in enumerate(tests):
    result = locate_cards(**test['input'])
    print(f"Test {i + 1}: {'Pass' if result == test['expected'] else f'Fail (got {result})'}")