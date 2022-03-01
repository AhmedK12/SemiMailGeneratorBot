import sqlite3


class Database:
    def __init__(self):
        self.DB_Name = "COUNT"
        self.Table = "Track"
        self.Email_id = "Email_id"
        self.Key = "Key"
        self.Count = 'Count'

        self.create()

    def create(self):
        try:
            self.conn = sqlite3.connect(self.DB_Name)
        except sqlite3.Error:
            print(sqlite3.Error)

        try:
            self.conn.execute(
                "CREATE TABLE " + self.Table + "(" + self.Key + " INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL," + self.Email_id + " TEXT  NOT NULL," + self.Count + " TEXT  );")

        except sqlite3.Error as e:
            print(e)
        self.conn.close()

    def open(self):
        return sqlite3.connect(self.DB_Name)

    def Insert_Emails(self, data, conn, values):
        try:
            conn.cursor().execute("INSERT INTO " + self.Table + data[0] + data[1], values)
            conn.commit()
        except sqlite3.Error as e:
            print(e)

    def Update_Emails(self, key, count, conn):
        conn.execute("UPDATE " + self.Table + " set Count= "+count+" WHERE Key ="+key+";")
        conn.commit()
        conn.close()

    def Delete_File(self, id):
        pass
