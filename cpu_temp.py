import psutil
import time
import os

filename = './cpu_log.txt' # Save data into file

try:
    sleep_time = int(input("> [Input]: Sleep time (Relaxation period between successive measurements): "))
except:
    print(f"> [User Error]: Must be an integer! {sleep_time} is an invalid command!")

try:
    try:
        with open(filename, 'w') as old_file:
            old_file.write(f"CPU Temperature Data - Argument sleep_time = {sleep_time}\n")
        print("> [Housekeeper]: Old file overwritten")
    except:
        print("> [Housekeeper]: Log file created")
        pass  

    time.sleep(1)

    def cpu_temp():
    	temps = psutil.sensors_temperatures()

    	if not temps:
    		return None

    	for name, entries in temps.items():
    		for entry in entries:
    			if entry.label == 'Package id 0':
    				return entry.current
    	return None

    def log_temperature(file_path):
        while True:

            temp = cpu_temp()

            if temp is None:
                print("> [Error]: Could not read CPU temperature")
                return

            if float(temp) >= 90:
                indicator = "!!! - Overheating"
            elif float(temp) >= 65 and float(temp) < 90:
                indicator = 'High'
            elif float(temp) >= 40 and float(temp) < 65:
                indicator = 'Normal'
            elif float(temp) < 40:
                indicator = 'Low'
            else:
                indicator = "Error - Out of Scale"  

            with open(file_path, 'a') as file:
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

                file.write(f"{timestamp} > {temp}°C\n")
                print(f"> {timestamp} >> [{indicator}] : {temp}°C")

                file.close()

            time.sleep(sleep_time)

    if __name__ == "__main__":
        log_temperature(filename)

except Exception as e:
    print(f"> [Severe Error]: {e}")        
