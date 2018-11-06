import schoolopy
import yaml

with open("example_config.yml", "r") as f:
    cfg = yaml.load(f)
    print(cfg, type(cfg))

sc = schoolopy.Schoology(schoolopy.Auth(cfg["key"], cfg["secret"]))
sc.limit = 10  # Only retrieve 10 objects max

userinfo = {
    "school_uid": "538118791",
    "name_first": "This_user_should_not_exist",
    "name_last": "null",
    "primary_email": "jasperwoodlaptop@gmail.com",
    "role_id": "318927",
    "additional_buildings":""
}

school = 538118791
print(sc._post("users",{"school_uid": "538118791","name_first": "This_user_should_not_exist","name_last": "null","primary_email": "jasperwoodlaptop@gmail.com","role_id": "318927","additional_buildings":""}))
#print(sc.update_user({school_id': 538118791, 'name_first': 'Daniel', 'primary_email': 'dmendelevitch2021@kehillahstudent.org', 'picture_url': 'https://cdn3-6.cdn.schoology.com/system/files/imagecache/profile_reg/sites/all/themes/schoology_theme/images/user-default.gif'},54473338))



