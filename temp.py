setting_file = open("_settings.txt", "r")
setting = {}
for line in setting_file:
    if line.split('=')[0].replace(' ',"") != 'activity_subject':
        value = line.split('=')[1].replace("\n","").replace(' ',"")
        setting[line.split('=')[0].replace(' ',"")] = value.replace(' ',"")
    else:
        value = line.split('=')[1].replace("\n","")
        setting[line.split('=')[0].replace(' ',"")] = value
    

print(setting)