import datetime

last_id = 0 #unique id for each note

class Note:
    '''
    Represent a note in the notebook.
    '''
    def __init__(self, memo, tags=''):
        '''
        Initialize a note with memo and optional space-separated tags.
        Automatically set the note's creation date and a unique id.
        '''
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filterr):
        '''
        Determine if this note amtches the filter text. Return True if matches,
        False otherwise. Search matches bothtext and tags.
        '''
        return filterr in self.memo or filterr in self.tags

class Notebook:
    '''
    Represent collection of notes that can be tagged, modified and searched.
    '''
    def __init__(self):
        '''
        Initialize a notebook with an empty list.
        '''
        self.notes = []

    def new_note(self, memo, tags=''):
        '''
        Create a new note and add it to the list.
        '''
        self.notes.append(Note(memo, tags))

    def _find_note(self, note_id):
        '''
        Locate the note with the given id.
        '''
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
        return None

    def modify_memo(self, note_id, memo):
        '''
        Find the note with the given id and change its memo to the given value.
        '''
        note = self._find_note(note_id)
        if note:
            note.memo = memo
            return True
        return False

    def modify_tags(self, note_id, tags):
        '''
        Find the note with the given id and change its tags to the given value.
        '''
        note = self._find_note(note_id)
        if note:
            note.tags = tags
            return True
        return False

    def search(self, filterr):
        '''
        Find all notes that match the given filter string.
        '''
        return [note for note in self.notes if note.match(filterr)]