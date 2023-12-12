from config import CONN, CURSOR

class Song:
    pass
    
    def __init__(self, name, album):
        self.id = None
        self.name = name
        self.album = album

    
    @classmethod
    def create_table(self):
        sql = '''CREATE TABLE IF NOT EXISTS songs(
            id INTEGER PRIMARY KEY,
            name TEXT,
            album TEXT
            )'''

        CURSOR.execute(sql)

    def save(self):
        
        sql = "INSERT INTO songs (name, album) VALUES (?, ?)"
        val = (self.name, self.album)

        CURSOR.execute(sql, val)

        self.id = CURSOR.execute(
            "SELECT last_insert_rowid() FROM songs").fetchone()[0]


    @classmethod
    def create(cls, name, album):
        # instance
        song = Song(name, album)
        song.save()
        return song