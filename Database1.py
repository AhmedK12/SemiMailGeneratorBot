import sqlite3


class Database:
    def __init__(self):
        self.DB_Name = "EMAIL"
        self.Table = "Emails"
        self.First_Name = "File_Name"
        self.Second_Name = "Second_Name"
        self.Password = "Password"
        self.Email_id = "Email_id"
        self.Date_Of_Birth = "Date_of_Birth"
        self.Recovery = 'Recovery'
        self.Key = "Key"
        self.Bitcoin_Conformation = "Bitcoin_Conformation"
        self.Google_Conformation = "Google_Conformation"

        self.create()

    def create(self):
        try:
            self.conn = sqlite3.connect(self.DB_Name)
        except sqlite3.Error:
            print(sqlite3.Error)

        try:
            self.conn.execute(
                "CREATE TABLE " + self.Table + "(" + self.Key + " INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL," + self.First_Name + " TEXT  ," + self.Google_Conformation + " TEXT  ," + self.Bitcoin_Conformation + " TEXT  ," + self.Second_Name + " TEXT  ," + self.Password + " TEXT  NOT NULL," + self.Email_id + " TEXT  NOT NULL,"+self.Recovery + " TEXT  ," + self.Date_Of_Birth + " TEXT  );")

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

    def Update_Emails(self, data, conn):
        conn.execute("UPDATE " + self.Table + "set " + data)


    def Delete_File(self, id):
        pass


