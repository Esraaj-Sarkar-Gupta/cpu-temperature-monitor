import os
import matplotlib.pyplot as plt
import time 

path = "/home/usr/directory/with/files"
filename = "/cpu_temp_log.txt"

filepath = path + filename

temps = []

with open(filepath , 'r') as file:
	lines = file.readlines()
for line in lines:

	if line == lines[0]: # First line holds special data
		arguments = line.split('=')
		sleep_time = int(arguments[1].strip())
		print(f"> [Data]: Argument sleep_time pulled to be {sleep_time} ")
		continue

	arguments = line.split(">")
	temp = arguments[1].split('°')[0]
	temps.append(float(temp))

t = 0
times = []
for _ in temps:
	times.append(t)
	t += int(sleep_time)

print(temps)
print(times)

plt.figure()

for i in range(len(temps)):

	temp = temps[i]

	if temp >= 90:
		colour = 'red'
	elif temp >= 70 and temp < 90:
		colour = 'orange'
	elif temp >= 40 and temp < 70:
		colour = 'green'
	elif temp < 40:
		colour = 'blue'
	else:
		colour = 'grey'

	plt.scatter(times[i] , temp , color = colour)

plt.ylabel("Temperature (°C)")
plt.xlabel("Time (s)")

plt.title("CPU Temperature")


plt.plot(times , temps , color = 'black')

plt.savefig("cpu_temp.png")

timename = time.time()
newfilepath = path + '/data' + '/cpu_temp_' + str(timename).split('.')[0] + '_log.txt'

try:
	os.rename(filepath , newfilepath)
except:
	print("> [Error]: Unable to save file into data saves")





