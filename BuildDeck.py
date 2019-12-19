
"""
Created on Thu Dec 19 08:38:43 2019

@author: phil
Automatically generate anki deck from sql database.
"""

import sqlite3
import genanki


# Open database and read data into local variables 
conn = sqlite3.connect('AnkiLyrics.db')
cursor = conn.cursor()
cursor.execute("select Line, Translation, Title from TranslatedLines;")
card_data = cursor.fetchall()

# Create a template for anki card
my_model = genanki.Model(
  1607392319,
  'Translate Lyrics',
  fields=[
    {'name': 'Lyric'},
    {'name': 'TranslatedLyric'},
    {'name': 'Song'}
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '{{Lyric}}',
      'afmt': '{{FrontSide}}<hr id="answer">{{TranslatedLyric}}',
      'tags': '{{Song}}'
    },
  ])



# Creates flashcards
notes = [ genanki.Note( 
  model = my_model,
  fields = data 
  ) for data in card_data ]



# add cards to new deck
my_deck = genanki.Deck(2059400110, 'Limon y Sal')
for note in notes:
    my_deck.add_note(note)

genanki.Package(my_deck).write_to_file('limon_y_sal.apkg')

#notes = [my_deck.add_note(my_note) ]