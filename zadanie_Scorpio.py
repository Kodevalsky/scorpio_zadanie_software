import psutil as psu
import time

def getLoad():
    stat = psu.cpu_percent(percpu = True)
    finalInfo = "Current CPU load per unit: \n"
    for enum in range(len(stat)):
        finalInfo += str(enum)+ "."+ str(stat[enum])+ "%\n"
    return finalInfo
        
        
def getTemp():
    stat = psu.sensors_temperatures()
    finalInfo = "Current CPU temperatures:\n"
    for name, entries in stat.items():
        finalInfo += name+ ": "
        for entry in entries:
            finalInfo += str(entry.current)+ " degrees Celcius\n"
    return finalInfo
        
def getMem():
    stat = psu.virtual_memory()
    finalInfo = "\nRAM total: "+ str(stat.total) + "\nRAM used: "+ str(stat.used) + "\nRAM avaible: "+ str(stat.available)
    return finalInfo
    

def getDisk():
    stat = psu.disk_usage("/")
    return "\nFree disk space: "+ str(stat.free) + "\n"
    
def getNet():
    stat = psu.net_if_stats()
    finalInfo = ""
    for nic, addr in psu.net_if_addrs().items():
        partNic = stat[nic]
        if partNic.isup:
            finalInfo += "Connection name: " + nic+ " Status: "+"UP "+ "IP Address: " + addr[0].address + "\n"
        else:
            finalInfo += "Connection name: " + nic+ " Status: "+"DOWN "+ "IP Address: " + addr[0].address + "\n"
    return finalInfo
            
def getBand():
    stat = psu.net_io_counters(pernic = True)
    finalInfo = ""
    for name in stat:
        initialBytesSent = stat[name].bytes_sent
        initialBytesRecv = stat[name].bytes_recv
        
        time.sleep(1)
        stat = psu.net_io_counters(pernic = True)
        endBytesSent = stat[name].bytes_sent
        endBytesRecv = stat[name].bytes_recv
        
        
        calcSpeedSent = endBytesSent - initialBytesSent
        calcSpeedRecv = endBytesRecv - initialBytesRecv
        finalInfo += name + " Current sending speed: "+ str(calcSpeedSent)+ " B/s Current receiving speed: "+ str(calcSpeedRecv) + " B/s\n"
    return finalInfo
        
    
    
while(True):
    time.sleep(3)
    infoFile = open("system_data_readings.txt", 'w')
    print(getLoad() + getTemp() + getMem() + getDisk() + getNet() + getBand())
    infoFile.write(getLoad() + getTemp() + getMem() + getDisk() + getNet() + getBand()) 