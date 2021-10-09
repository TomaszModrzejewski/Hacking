import csv
from db_connection import DbConnection

def load():
  db_conn = DbConnection('skillneeds')

  db_conn.execute("drop table if exists skillneeds")
  db_conn.execute("create table skillneeds (id integer PRIMARY KEY, year integer not null, isic_section_index text not null, isic_section_name text not null, industry_name text not null, skill_group_category text not null, skill_group_name text not null, rank integer not null)")

  id = 1

  with open('./data/public_use-industry-skills-needs.csv', newline='') as csvfile:
    skillreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in skillreader:
      if row[0] == "":
        continue
      row.insert(0, id)
      db_conn.execute("insert into skillneeds values (?, ?, ?, ?, ?, ?, ?, ?)", row)
      id = id + 1
      db_conn.commit()

  db_conn.close()