
ip=[
{"PID": 51207, "IP": "192.168.0.88"},
{"PID": 25783, "IP": "127.0.1.1"},
{"PID": 62919, "IP": "192.168.0.121"}
]

def find_next_ip(ip_list,random_number):
    length=len(ip_list)
    address=[]
    flag=0
    for i, current_entry in enumerate(ip_list):
      
        if current_entry['PID']==random_number:
            if i==0:
                if(i+1!=length):address.append(ip_list[i+1]['IP'])
                address.append(ip_list[i]['IP'])
                flag=0
            elif i==length-1:
                address.append(ip_list[i-1]['IP'])
                address.append(ip_list[i]['IP'])
                flag=2
            else:
                address.append(ip_list[i-1]['IP'])
                address.append(ip_list[i+1]['IP'])
                address.append(ip_list[i]['IP'])
                flag=1



    return address,flag


       
       
#print(find_next_ip(ip,62919))    
        