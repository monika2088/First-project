import os
os.getcwd()
f=open("test.txt",'r')
g=open("error.txt",'w')
h=open("warnings.txt",'w')
for line in f:
    if "error" in line:
        g.write(line)
    if "warning" in line:
        h.write(line)
        
f.close()
g.close()
h.close()
