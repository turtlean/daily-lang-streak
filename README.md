TODO:
- Add SQLite to python's project 
- Add second account to GitHub
- Think a better name for the project

English dict: 3 consecutive lines

Python!

SQLite database
Very little configuration
Extremely portable
Export to .yml or .json
Regular backups


This makes me think it's possible


find(expression: "string", keywords: Array of ::String) : {"expression": String, "translation": String, "example": String, keywords: [String]}
  - checks if first argument is included in expression
  - checks if all of the keywords are included in any of translation, example or keywords


test(level)
  - asks if you want to display hint/context
  - asks if it's correct or not:
    - score 1: 0-3
    - score 2: 3-5
    - score 3: 5
    - score 0: Maintenance (> 5)
  - update score:
    - if correct: score += 1
    - if incorrect: score -= 1


add(expression, context, translation or meaning, single example, keywords)

update(id, field)

Same expressions with different meanings have separate entries
0. entry_id
1. expresion (to be learned) [First param]
2. context or hint: context where I've learned that word (optional)
3. translation or meaning [Second param]
4. Single example [Second param]
5. Extra information
6. Keywords (to easily look for it) [Second param]

First step is transforming YML into JSON
Eventually, it will become a huge file. I know that. But it's ok.

Challenge is

