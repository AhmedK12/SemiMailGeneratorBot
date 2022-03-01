import Database

database = Database.Database()


def Insert_Email(Email_id, Count):
    conn = database.open()
    data = [
        " (" + database.Email_id + ","+database.Count+ " )",
        " VALUES ( :" + database.Email_id + ", :"  + database.Count+" ) "]

    values = {database.Email_id: Email_id,
              database.Count:Count}
    database.Insert_Emails(data, conn, values)
    conn.close()


def fetch_Email():
    conn = database.open()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Track")

    rows = cur.fetchall()
    conn.close()
    return rows


def find_id(email):
    conn = database.open()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Track")
    rows = cur.fetchall()
    conn.close()

    for row in rows:
        if row[1] == email:
           return row[0]

def find_count(email):
    conn = database.open()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Track")
    rows = cur.fetchall()
    conn.close()

    for row in rows:
        if row[1] == email:
           return row[2]


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


def update(email):
    conn = database.open()
    database.Update_Emails(str(find_id(email)),str(int(find_count(email))+1), conn)


if __name__ == '__main__':
    update('b180113@nitsikkim.ac.in#$b180113@nitsikkim.ac.in')
    for i in fetch_Email():
        print(i)