import schoolopy
import yaml

with open('example_config.yml', 'r') as f:
    cfg = yaml.load(f)
    print(cfg, type(cfg))

sc = schoolopy.Schoology(schoolopy.Auth(cfg['key'], cfg['secret']))
sc.limit = 10  # Only retrieve 10 objects max

receps = "54473320"

message = sc._post("messages",{"subject":"Secret info","message":"They call me bot man","recipient_ids": receps})
print(message, type(message))


"""
message = sc.send_message('bot message','content',['54473364'])
message.recipient_ids = [str(myid)]
message.subject = 'test'
message.content = 'this message was sent by a bot'
"""
#print(message)
"""
print('Your name is %s' % sc.get_me().name_display)
for update in sc.get_feed():
    user = sc.get_user(update.uid)
    print('By: ' + user.name_display)
    print(update.body[:40].replace('\r\n', ' ').replace('\n', ' ') + '...')
    print('%d likes\n' % update.likes)
"""