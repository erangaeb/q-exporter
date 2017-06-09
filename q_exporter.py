import csv

configs = csv.reader(open('s_configs.csv', 'r'))
for config in configs:
    q = "INSERT INTO " \
            "sconf (intermediatorid, sendconfigs_id, validatelegalattachments, digsigtype) " \
            "values (%s, %s, %s, %s)" % (config[0], config[1], config[2], config[3])
    print q
