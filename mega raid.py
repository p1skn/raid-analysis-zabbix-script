import subprocess
import re
import sys
# path to mega raid console app (storcli64, not megacli) 
PATH = "c:\\script\\storcli64.exe"


def get_data_disks(num):
    try:
        output = subprocess.check_output([PATH, "/c0/e252/s" + str(num), "show"], universal_newlines=True).split('\n')
        if output[4] == "Description = No drive found!":
            return "error"
        else:
            return output
    except subprocess.CalledProcessError as e:
        print("Error:", e)
        sys.exit(1)

def get_data_controler():
    try:
        output = subprocess.check_output([PATH, "/c0", "show"], universal_newlines=True)
        return output
    except subprocess.CalledProcessError as e:
        print("Error:", e)
        sys.exit(1)

def get_status_controller(data):
    for line in data.split('\n'):
        if "Status = " in line:
            status = line.split('=')[1]
            if status != " Success":
                return 1
    return 0

def get_status_volume(data):
    VD = 0
    for line in data.split('\n'):
        if "Virtual Drives = " in line:
            num_VD = line.split('=')[1]
    pattern = r"(?<=VD LIST :).*?(?=VD=Virtual Drive)"
    matches = re.search(pattern, data, re.DOTALL)
    if matches:
        for line in matches.group(0).split('\n'):
            if "Optl" in line:
                VD += 1
        if VD != int(num_VD):
            return 1
    return 0

def get_status_disk(data):
    media_error = other_error = predictive_error = 0
    pattern = r"(?<=Description =).*?(?=EID=)"
    matches = re.search(pattern, '\n'.join(data), re.DOTALL)
    if matches:
        if "Onln" not in matches.group(0):
            return 1
    for i in data:
        media_error_match = re.search(r'Media Error Count =\s*(\w+)', i)
        other_error_match = re.search(r'Other Error Count =\s*(\w+)', i)
        predictive_error_match = re.search(r'Predictive Failure Count =\s*(\w+)', i)

        if media_error_match:
            media_error = int(media_error_match.group(1))
        if other_error_match:
            other_error = int(other_error_match.group(1))
        if predictive_error_match:
            predictive_error = int(predictive_error_match.group(1))
    if media_error != 0 or other_error != 0 or predictive_error != 0:
        return 1 
    return 0  


if __name__ == "__main__":
    data_controler = get_data_controler()
    err = get_status_controller(data_controler) + get_status_volume(data_controler)

    i = 0
    stop = False

    while not stop:
        output = get_data_disks(i)
        if output != "error" and i < 20:
            err += get_status_disk(output)
        else:
            stop = True
            break
        i += 1

    if err != 0:
        print(1)
    else:
        print(0)
    #pva :D
