# SpAnki
Automatic translation and Anki flash card creation from Spanish lyrics. Inspired by immersion methods for language learning, this script turns your favorite spanish song lyrics into Anki flashcards to help consolidate vocab.  

# To Use
1) Save songs as .txt files to folder Songs
2) Run ScrapeAndTranslate.py. This take the information from the .txt files, translates each song line, and creates a sql database AnkiLyrics.db (note that this will run with errors if AnkiLyrics.db already exists in the same folder).
3) Edit AnkiLyrics.db directly if necessary (some of the translations will be naff).
4) Run BuildDeck.py. This takes the information AnkiLyrics.db and creates flashcards which can be loaded by Anki. 
