import sys
from flow import test_me_flow, definition_flow, add_flow, count_flow

argv = sys.argv[1:]

if (len(argv) < 1):
  print("Options:'test [level]' or 'remind [expression]'")
elif (argv[0] == 'test'):
  level = argv[2] if len(argv) > 2 else 0
  test_me_flow(level)
elif (argv[0] == 'definition'):
  keyword = argv[2] if len(argv) > 2 else None
  definition_flow(argv[1], keyword)
elif (argv[0] == 'add'):
  add_flow()
elif (argv[0] == 'count'):
  count_flow()
else:
  print("Options:'test [level]' or 'remind [expression]'")
