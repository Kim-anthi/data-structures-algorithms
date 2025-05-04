# def locate_cards(cards, query):
#   #create a variable position with value 0
#   position = 0
  
#   #loop
#   while True:
#     #check element at current position meets the query
#     if cards[position] == query:
#       #return the position and quit
#       return position
#     #increasing the potion
#     position += 1
    
#     #check the end of an array
#     if position == len(cards):
#       #return -1 if no number found
#       return -1
    

 
 
 # ----> shorter piece of code   
# def locate_card(card, query):
#   position = 0
#   while position < len(cards):
#     if cards[position] == query:
#       return position
#     position +=1
#   return -1


#For complexity if the cards are sorted we pick a card in the middle and 
#this helps eliminate others cards reducing time 
# (((BINARY SEARCH)))


#---> so this reduces time complexity
def locate_cards(cards, query):
  lo, hi = 0, len(cards) - 1
  
  while lo <= hi: 
    mid = (lo + hi) // 2
    mid_number = cards[mid]
    
    print("lo:", lo, ", hi:", hi, ", mid:", mid, ", mid_number:", mid_number)
    
    if mid_number == query:
      return mid
    elif mid_number < query:
      hi = mid - 1
    elif mid_number > query:
      lo = mid + 1
  return -1 


   

# -------> for duplicate elements
def test_location(cards, query, mid):
  if cards[mid] == query:
    if mid - 1 >= 0 and cards[mid-1] == query:
      return 'left'
    else:
      return 'found'
  elif cards[mid] < query:
    return 'left'
  else:
    return 'right'

def locate_card(cards, query):
  lo, hi = 0, len(cards) - 1
  while lo <= hi:
    mid = (lo + hi) // 2
    result = test_location(cards, query, mid)
    if result == 'found':
      return mid
    elif result == 'left':
      hi = mid - 1
    elif result == 'right':
      lo = mid + 1
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
    },
     {
        'input': {'cards': [13, 11, 11, 11, 10, 7, 4], 'query': 11},
        'expected': 1   
    }
]


for i, test in enumerate(tests):
    result = locate_cards(**test['input'])
    print(f"Test {i + 1}: {'Pass' if result == test['expected'] else f'Fail (got {result})'}")
 