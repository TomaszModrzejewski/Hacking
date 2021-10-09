import sqlite3

class DbConnection:
  path_to_data = './data/'
  db_extension = '.db'

  db_connection = None

  def __init__(self, db_name):
    self.db_connection = sqlite3.connect(self.path_to_data + db_name + self.db_extension)

  def execute(self, command, parameters=None):
    if parameters is None:
      return self.db_connection.cursor().execute(command)
    else:
      return self.db_connection.cursor().execute(command, parameters)

  def close(self):
    self.db_connection.close()
  
  def commit(self):
    self.db_connection.commit()