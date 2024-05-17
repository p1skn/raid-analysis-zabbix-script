import subprocess
import re
import sys
# path to intel raid console app (IntelVROCCli) 
PATH = "c:\\script\\7.0.0_IntelVROCCli.exe"

def get_status():
    try:
        output = subprocess.check_output([PATH, "--information"], universal_newlines=True).split('\n')
        return output
    except subprocess.CalledProcessError as e:
        print("Error:", e)
        sys.exit(1)

def get_state_status(output):
    all_disks_normal = True
    for i in output:
        state_match = re.search(r'State:\s*(\w+)', i)
        if state_match:
            state = state_match.group(1)
            if state != "Normal":
                all_disks_normal = False
    if all_disks_normal:
        return 0
    else:
        return 1



if __name__ == "__main__":
    handler = get_status()
    state_status = get_state_status(handler)
    if state_status == 1:
        print(1)
    else:
        print(0)
    #pva :D
