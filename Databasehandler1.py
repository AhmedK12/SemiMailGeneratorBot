import Database1

database = Database1.Database()


def Insert_Email(First_Name, Second_Name, Email_id, Password, Birth_Date, Google_conformation, Bitcoin_conformation,Recovery):
    conn = database.open()
    data = [
        " (" + database.First_Name + "," + database.Second_Name + "," + database.Email_id + "," + database.Password + "," + database.Date_Of_Birth + "," + database.Google_Conformation + "," + database.Bitcoin_Conformation +"," +database.Recovery+ " )",
        " VALUES ( :" + database.First_Name + ",:" + database.Second_Name + ", :" + database.Email_id + ", :" + database.Password + ", :" + database.Date_Of_Birth + ", :" + database.Google_Conformation + ", :" + database.Bitcoin_Conformation +", :"+ database.Recovery+" ) "]

    values = {database.First_Name: First_Name, database.Second_Name: Second_Name, database.Email_id: Email_id,
              database.Password: Password, database.Date_Of_Birth
              : Birth_Date, database.Google_Conformation: Google_conformation,
              database.Bitcoin_Conformation: Bitcoin_conformation,database.Recovery:Recovery}
    database.Insert_Emails(data, conn, values)
    conn.close()


def fetch_Email():
    conn = database.open()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Emails")

    rows = cur.fetchall()
    conn.close()
    return rows


def find_id(email):
    conn = database.open()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Emails")
    rows = cur.fetchall()
    conn.close()
    ids = []
    for row in rows:
        if row[6] == email:
           ids.append(row[0])
    return ids

def find_password(email):
    rows = fetch_Email()
    for row in rows:
        if row[6]==email:
            return row[5]

def delete_email(ids):
    """
    Delete a task by task id
    :param conn:  Connection to the SQLite database
    :param id: id of the task
    :return:
    """
    conn = database.open()
    try:
        sql = 'DELETE FROM Emails WHERE Key=?'
        cur = conn.cursor()
        for id in ids:
            cur.execute(sql, (id,))
            conn.commit()
    except:
        pass
    conn.close()


if __name__ == '__main__':
    fetch_Email()

