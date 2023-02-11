import paramiko
import re
import time
username = input('Username: ')
password = input('Password: ')
lab_ip = input('CML IP Address: ')
lab_id = input('Lab ID: ')

# create SSH client
print("Make sure all the TTYs are open on CML!!\n(just press enter a couple times)")
input("Press enter to confirm all terminals are ready.")
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print("Connecting to: "+lab_ip)
# connect to lab
client.connect(lab_ip, username=username, password=password,look_for_keys=False)

# get list of nodes in lab
command='list'
print("Executing: "+command)
_, stdout, _ = client.exec_command(command,get_pty=True)
print(command+" executed!")
output=stdout.read()
print(str(output,'utf-8'))
output_str=str(output,'utf-8')
nodes_regex = r"n\d{1,2}"
nodes=re.findall(nodes_regex, output_str)
print(nodes)



# iterate over nodes and run command

for node in nodes:
    print("[*] Starting Commands for node: "+node)
    channel = client.invoke_shell()
    open_command="open "+"/"+lab_id+"/"+node+"/0"+"\n"
    node_command="sh run\n" 
    while channel.send_ready()==False:
        time.sleep(1)
    channel.send(open_command)
    time.sleep(3)
    channel.send("\n")
    channel.send("\n")
    channel.send("\n")
    channel.send("\n")
    while channel.send_ready()==False:
        time.sleep(1)
    channel.send("en")
    channel.send("\n")
    while channel.send_ready()==False:
        time.sleep(1)
    channel.send("term len 0")
    channel.send("\n")
    time.sleep(2)
    while channel.send_ready()==False:
        time.sleep(1)
    channel.send(node_command)
    time.sleep(10)
    while channel.recv_ready()==False:
        time.sleep(1)
    response=channel.recv(9999).decode()
    print(response)
    with open(node+"_config.txt",'w+') as file:
        file.write(response)
        print("[*] File written for node: "+node)
        file.close()
    channel.close()

# close SSH connection
print("[*] Command Execution finished!")
client.close()
