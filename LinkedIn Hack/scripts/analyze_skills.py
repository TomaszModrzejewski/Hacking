import argparse
import profile
import scoring
import sys

parser = argparse.ArgumentParser()
parser.add_argument('--id', '-i', help="The id of the profile", type= int, default= 0)
parser.add_argument('--name', '-n', help="The name of the profile", type= str)
args=parser.parse_args()

if args.id == 0 and args.name is None:
  print('Specify either the --id or the --name of the profile to analyze')
  exit()

industry_to_total_score_dict = {}

profiles_to_analyze = profile.get_profiles_by_id_or_name(args.id, args.name)

for profile_to_analyze in profiles_to_analyze:
  if profile_to_analyze is None:
    print('This profile does not exist')
    exit()

  #skills_array = ['Computer Networking', 'Software Development Life Cycle (SDLC)', 'Mathematics']

  print("\n\n\n\n")
  print("----------", "Matching skills for profile:", "----------")
  profile_to_analyze.print()
  print("--------------------------------------------------\n")

  industry_to_needs_list_dict = scoring.get_industry_to_needs_list()
  industry_to_skill_pen_list_dict = scoring.get_industry_to_skill_pen_list()

  for key, value in industry_to_needs_list_dict.items():
    similarity = scoring.jaccard(profile_to_analyze.skills, value)
    pen_score = scoring.calculate_pen_score(industry_to_skill_pen_list_dict, key, profile_to_analyze.skills) 
    total_score = similarity * pen_score * 100
    if total_score > 0:
      industry_to_total_score_dict[key] = total_score

  for key, value in sorted(industry_to_total_score_dict.items(), key = lambda item: item[1], reverse = True):
    print(' > ', key, "-- Match Score: ", value)
