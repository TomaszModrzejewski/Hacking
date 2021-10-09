# LinkedIn Hack

For an initial load, run `python3 dbload.py`.

There are 1000 profiles with random name and 4 skills in their skillset.

To analyze the skills of a profile, run:
`python3 analyze_skills.py --id [ID]`
where `[ID]` is an integer from 1 to 1000.

or
`python3 analyze_skills.py --name "[NAME]"`
where `[NAME]` can be a full or partial name, e.g. Hillary Velasquez
