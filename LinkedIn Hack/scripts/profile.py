from db_connection import DbConnection

PROFILE_ID_COL_INDEX = 0
PROFILE_NAME_COL_INDEX = 1
PROFILE_SKILLSET_COL_INDEX = 2
PROFILE_CONNECTION_WEIGHT_COL_INDEX = 3

def get_profiles_by_id_or_name(id=0,profile_name=None):
  if id == 0 and profile_name is None:
    return None

  if profile_name is not None:
    profile_name = '%' + profile_name + '%'

  db_conn = DbConnection('profiles')

  profiles = []

  for row in db_conn.execute('select * from profiles where id=? or name like ?;', (id, profile_name)):
    profiles.append(Profile(row[PROFILE_ID_COL_INDEX], row[PROFILE_NAME_COL_INDEX], row[PROFILE_SKILLSET_COL_INDEX], row[PROFILE_CONNECTION_WEIGHT_COL_INDEX]))

  db_conn.close()

  return profiles

class Profile:
  id = 0
  name = None
  connection_weight = 0
  skills = []
  skillset_delimiter = ','

  def __init__(self, id, name, skillset, connection_weight):
    self.id = id
    self.name = name
    self.skills = skillset.split(self.skillset_delimiter)
    self.connection_weight = connection_weight
    pass

  def print(self):
    print('    id: ', self.id)
    print('    name: ', self.name)
    print('    skillset: ', ', '.join(self.skills))
    print('    connections weight: ', self.connection_weight)