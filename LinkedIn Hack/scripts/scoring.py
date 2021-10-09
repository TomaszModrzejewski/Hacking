from db_connection import DbConnection
from collections import defaultdict

COL_INDEX_SKILL_NEEDS_ID = 0
COL_INDEX_SKILL_NEEDS_YEAR = 1
COL_INDEX_SKILL_NEEDS_SECTION_INDEX = 2
COL_INDEX_SKILL_NEEDS_SECTION_NAME = 3
COL_INDEX_SKILL_NEEDS_INDUSTRY_NAME = 4
COL_INDEX_SKILL_NEEDS_SKILL_GROUP_CATEGORY = 5
COL_INDEX_SKILL_NEEDS_SKILL_GROUP_NAME = 6
COL_INDEX_SKILL_NEEDS_RANK = 7

COL_INDEX_SKILL_PEN_ID = 0
COL_INDEX_SKILL_PEN_YEAR = 1
COL_INDEX_SKILL_PEN_SKILL_GROUP_CATEGORY = 2
COL_INDEX_SKILL_PEN_SKILL_GROUP_NAME = 3
COL_INDEX_SKILL_PEN_SECTION_INDEX = 4
COL_INDEX_SKILL_PEN_SECTION_NAME = 5
COL_INDEX_SKILL_PEN_INDUSTRY_NAME = 6
COL_INDEX_SKILL_PEN_RATE = 7

def jaccard(list1, list2):
  intersection = len(list(set(list1).intersection(list2)))
  union = (len(list1) + len(list2)) - intersection
  return float(intersection) / union

def calculate_pen_score(pen_rate_dict, industry, skills_list):
  match_any = False
  score = 1
  industry_rates = pen_rate_dict[industry]
  for my_skill in skills_list:
    if my_skill in industry_rates:
      score = score * (industry_rates[my_skill] * 100)
      match_any = True
  if match_any:
    return score
  else:
    return 0.0

def get_industry_to_needs_list():
  db_conn = DbConnection('skillneeds')
  industry_to_needs_list_dict = defaultdict(list)

  # Get latest
  for row in db_conn.execute('select * from skillneeds where year = "2019"'):
    industry_to_needs_list_dict[str(row[COL_INDEX_SKILL_NEEDS_INDUSTRY_NAME])].append(str(row[COL_INDEX_SKILL_NEEDS_SKILL_GROUP_NAME]))

  db_conn.close()

  return industry_to_needs_list_dict

def get_industry_to_skill_pen_list():
  db_conn = DbConnection('skillpen')

  industry_to_skill_pen_list_dict = defaultdict(lambda: defaultdict(int))

  for row in db_conn.execute('select * from skillpenetration where year = "2019"'):
    industry_to_skill_pen_list_dict[str(row[COL_INDEX_SKILL_PEN_INDUSTRY_NAME])][str(row[COL_INDEX_SKILL_PEN_SKILL_GROUP_NAME])] = row[COL_INDEX_SKILL_PEN_RATE]

  db_conn.close()

  return industry_to_skill_pen_list_dict