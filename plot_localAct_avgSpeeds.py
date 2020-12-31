import sys
import os
import json
import datetime
from pylab import *

# pass activity directory as command-line argument!
# pass the year of concern as second command-line argument

data_dict = {}
ids = []
avg_speeds = []
avg_watts = []
tot_kcal = []
for root, dirs, files in os.walk(str(sys.argv[1]), topdown=True):
    for act_filename in files:
        with open(os.path.join(root, act_filename)) as act_file:
            act_json = json.load(act_file)
            if act_json['start_date'].split('T')[0].split('-')[0] != sys.argv[2]:
                continue
            print(act_json['start_date'])
            try:
                gear_name = act_json['gear']['name']
            except:
                gear_name = None
            if gear_name and not act_json['commute']:
                if not gear_name in data_dict.keys():
                    data_dict[gear_name] = [[], [], [], []] # date, speed, watts, kcal
                data_dict[gear_name][0].append(datetime.datetime.strptime(act_json['start_date'].split('T')[0], '%Y-%m-%d'))
                data_dict[gear_name][1].append(3.6*act_json['average_speed'])
                data_dict[gear_name][2].append(act_json['average_watts'])
                data_dict[gear_name][3].append(act_json['calories'])

figure()
leg_list = []
for gear_name in data_dict:
    leg_list.append(gear_name)
    plot(data_dict[gear_name][0], data_dict[gear_name][1], 'o')
legend(leg_list)

figure()
leg_list = []
for gear_name in data_dict:
    leg_list.append(gear_name)
    plot(data_dict[gear_name][0], data_dict[gear_name][2], 'o')
legend(leg_list)

show()
