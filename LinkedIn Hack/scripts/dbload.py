import dbload_profiles
import dbload_skillneeds
import dbload_skillpen

print('-- Loading the DB --')
print('-- profiles...')
dbload_profiles.load()
print('-- skill needs...')
dbload_skillneeds.load()
print('-- skill pen...')
dbload_skillpen.load()
print('-- Done --')