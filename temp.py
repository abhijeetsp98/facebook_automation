group_list = []
group_file = open("_post_id.txt", "r")
for line in group_file:
    group_list.append(line.replace("\n",""))
print(group_list[0])