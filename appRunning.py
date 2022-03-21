import wmi
  
# Initializing the wmi constructor
f = wmi.WMI()
  
flag = 0
  
# Iterating through all the running processes
for process in f.Win32_Process():
    if "Code.exe" == process.Name:   #WhatsApp.exe, msedge.exe, Code.exe
        print("Application is Running")
        flag = 1
        break
  
if flag == 0:
    print("Application is not Running")