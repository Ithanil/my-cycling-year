import sys
import os
import json
from pylab import *

# pass activity directory as command-line argument!

data_dict = {}
ids = []
avg_speeds = []
avg_watts = []
for root, dirs, files in os.walk(str(sys.argv[1]), topdown=True):
    for act_filename in files:
        with open(os.path.join(root, act_filename)) as act_file:
            act_json = json.load(act_file)
            try:
                gear_name = act_json['gear']['name']
            except:
                gear_name = None
            if gear_name:
                print(gear_name)
                if not gear_name in data_dict.keys():
                    data_dict[gear_name] = [[], [], []] # id, speed, watts
                data_dict[gear_name][0].append(act_json['id'])
                data_dict[gear_name][1].append(3.6*act_json['average_speed'])
                data_dict[gear_name][2].append(act_json['average_watts'])

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
