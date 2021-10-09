from db_connection import DbConnection

db_conn = DbConnection('skillneeds')

for row in db_conn.execute('select count(*) from skillneeds'):
  print(row)

db_conn.close()

