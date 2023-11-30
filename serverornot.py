
ip=[
{"PID": 51207, "IP": "192.168.0.88"},
{"PID": 25783, "IP": "127.0.1.1"},
{"PID": 62919, "IP": "192.168.0.121"}
]


def serveryorn(ip_list,random_number):
    for i, current_entry in enumerate(ip_list):

        if current_entry['PID']==random_number:
            if i==0 :
                return 0
            else:
                return 1 
