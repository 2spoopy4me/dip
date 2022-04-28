#! /usr/bin/env python3.
# database interface program

'''16gb db is too big to load into memory, need
to figure out how you can parse and load into memory.
Start by sifting through and only selecting column
names - from there you can spider the db, only adding
to memory/dictionary what values are from the column
specified'''


class Dip:
    def __init__(self, filename):
        self.filename = filename

    def get_columns():
        '''Loads columns into memory'''
        pass
    
    def get_rows(str: column, limit=None):
        '''Loads all rows into memory'''
        pass
