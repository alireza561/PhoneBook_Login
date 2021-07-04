import sqlite3

class ViewContacts():
    """ This class displays all saved members in the treeview 
    and
    First of all, in order for the members to be displayed regularly, we have to delete them all at once
    """
    def view_command(self):
         self.tree.delete(*self.tree.get_children()) 
         conn = sqlite3.connect("My_PhoneBook.db")
         cursor = conn.cursor()
         cursor.execute("SELECT * FROM member")
         fetch = cursor.fetchall()
         for data in fetch:
            self.tree.insert('', 'end', values=data)
         cursor.close()
         conn.close()