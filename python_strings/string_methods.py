import time
import re


msg = "GhostNet#X44CR#98.654#TRC8821-0XGhngtr64%fR$"

''' 
format this using the arrangement method below, using the .split() method


CodeName:    | GhostNet
MessageCode: | X44CR
lastletter:  | R
TraceID:     | TRC8821
Traceable:   | Yes
severityLevel| 98.65
'''

print(msg'\n')

time.sleep(2)

new = re.split(r"[#-]", msg)

print(new)

#print(new_msg[1])

#print(f"
