from pylab import *
import datetime

def month_str_to_number(month_str):
    months = {"Jan" : 1, "Feb" : 2, "Mrz" : 3, "Apr" : 4, "Mai" : 5, "Jun" : 6, "Jul" : 7, "Aug" : 8, "Sep" : 9, "Okt" : 10, "Nov" : 11, "Dez" : 12}
    return months[month_str]

dates = []
weights = []

trigger = False
with open(str(sys.argv[1])) as weight_file:
    for line in weight_file:
        if line[1] == " ":
            dates.append(datetime.date(int(line.split()[3].split('"')[0]), month_str_to_number(line.split()[2]), int(line.split()[1])))
            trigger = True
        else:
            if trigger:
                weights.append(float(line.split(',')[1].split()[0]))
                trigger = False
            else:
                print("Note: Duplicate weight data line. The line was:")
                print(line)                
print(dates)
print(weights)

plot(dates, weights, 'o')
show()
