import sys
from dictionary import find_random_expression, definition, print_dictionary_entries, update_score

def test_me_flow(score):
  random_expression = find_random_expression(score)
  print ('\n  %s  \n' %(random_expression))
  result = input("Correct?: (y)es / (n)o   ").upper()
  if result[0] == 'Y':
    update_score(random_expression, 1)
    print("Well done! Your score is +1")
  elif result[0] == 'N':
    update_score(random_expression, -1)
    print("Let's keep practising! Your score is -1")
  else:
    print("Invalid result")

argv = sys.argv[1:]

if (len(argv) < 1):
  print("Options:'test [level]' or 'remind [expression]'")
elif (argv[0] == 'test'):
  if len(argv) < 2: 
    print("Missing level on testing expression")
  else:
    test_me_flow(argv[1])
elif (argv[0] == 'definition'):
  keyword = argv[2] if len(argv) > 1 else None
  print_dictionary_entries(definition(argv[1], keyword))
else:
  print("Options:'test [level]' or 'remind [expression]'")
