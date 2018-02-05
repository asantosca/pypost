import sys

target=sys.argv[1]

a = "{{protocol}}://{{uaa-host}}/oauth/token"


filepath = f'./{target}/settings'  
with open(filepath) as fp:  
   line = fp.readline()
   while line:
       data = line.rstrip('\n').split(":",2)
       a = a.replace("{{" + data[0] + "}}", data[1])
       line = fp.readline()

