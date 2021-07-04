import sqlite3
class Insert:
    """ This class adds the user to the database """
    def insert(self):
        conn = sqlite3.connect("Login.db")
        cur = conn.cursor()

        self.sing_up_eror.set('')
        cur.execute("INSERT INTO loginpage (username, password) VALUES (?, ?)",
                        (str(self.usereg_entry.get()), str(self.passreg_entry.get())))
        conn.commit()
        conn.close()