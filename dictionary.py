import copy
import json
import os
import random
import sqlite3
from collections import OrderedDict

dir_path = os.path.dirname(os.path.realpath(__file__))
DB_FILENAME = dir_path + '/' + 'dictionary.db'

def find_random_entry(level):
  conn = sqlite3.connect(DB_FILENAME)

  c = conn.cursor()
  c.execute("SELECT id from entries")
  ids = list(map(lambda x: x[0],c.fetchall()))

  random_id = random.choice(ids)
  c.execute("""
    SELECT id, expression, context, meaning, example, extra, keywords, score 
    FROM entries
    WHERE id = ?
    """, (random_id,)
  )
  t = c.fetchone()
  entry_dict = tuple_to_dict(t)

  c = conn.cursor()
  conn.close()
  return entry_dict

def tuple_to_dict(entry):
  return {
    'id': entry[0],
    'expression': entry[1],
    'context': entry[2],
    'meaning': entry[3],
    'example': entry[4],
    'extra': entry[5],
    'keywords': entry[6],
    'score': entry[7]
  }

def find_entry(expression, keyword):
  expression = '%' + expression + '%'
  keyword = '%' + keyword + '%' if keyword else expression

  conn = sqlite3.connect(DB_FILENAME)
  c = conn.cursor()
  c.execute("""
    SELECT id, expression, context, meaning, example, extra, keywords, score
    FROM entries
    WHERE expression LIKE (?)
    OR keywords LIKE (?)
  """, (expression, keyword,))

  tuples = c.fetchall()
  conn.close()
  return list(map(lambda t: tuple_to_dict(t), tuples))

def update_score(entry_id, score):
  conn = sqlite3.connect(DB_FILENAME)

  c = conn.cursor()
  c.execute("""
    UPDATE entries
    set score = ?
    where id = ?
  """, (score, entry_id,))

  conn.commit()
  conn.close()

def add_entry(expression, context, meaning, example, extra, keywords):
  conn = sqlite3.connect(DB_FILENAME)

  c = conn.cursor()
  c.execute("""
    INSERT INTO entries 
    (expression,context,meaning,example,extra,keywords,score) 
    VALUES 
    (?,?,?,?,?,?,?)
  """, (expression, context, meaning, example, extra, keywords, 0,))

  conn.commit()
  conn.close()

def print_entry(e):
  print('\n')
  print ('  Expression:  %s  ' %(e["expression"].capitalize()))
  print ('  Context:  %s  ' %(e["context"]))
  print ('  Meaning:  %s  ' %(e["meaning"]))
  print ('  Example:  %s  ' %(e["example"]))
  print ('  Extra:  %s  ' %(e["extra"]))
  print ('  Keywords:  %s  ' %(e["keywords"]))
  print ('  Score:  %s  ' %(e["score"]))
  print('\n')

def count():
  conn = sqlite3.connect(DB_FILENAME)
  c = conn.cursor()
  c.execute("SELECT COUNT(*) from entries")
  count = c.fetchone()[0]
  conn.close()
  return count
