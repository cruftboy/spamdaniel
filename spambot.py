import schoolopy
import yaml
import time
import random

with open('example_config.yml', 'r') as f:
    cfg = yaml.load(f)
    print(cfg, type(cfg))

sc = schoolopy.Schoology(schoolopy.Auth(cfg['key'], cfg['secret']))
sc.limit = 1000  # Only retrieve 10 objects max

subjects = ["[Advisory: Section 6]","[AP Calculus AB: Block 2]","[AP Computer Science A: Block 6]","[Chemistry Honors: B1]","[Holocaust Historical Perspectives: Section 1]","[Precalculus Honors: Block 3]","[Reflective Practice : Meditation]","[Responding to Lit Honors: B8]","[Spanish 4 Honors: Section 1]","[World History 2: Block 4]"]

receps = "54473364"
#54473338

for i in range(1000):
	subpick = random.randrange(0,9,1)
	wait = random.randrange(60,3600,1)
	print(wait)
	time.sleep(wait)
	message = sc._post("messages",{"subject":subjects[subpick] + " Important info for next class","message":"For the next class period there will be no homework. The homework that was assigned will instead be due next week. \n \n \n spam","recipient_ids": receps})
	print(message, type(message))
