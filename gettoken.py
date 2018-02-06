
a = "{{protocol}}://{{uaa-host}}/oauth/token"


# load settings

kv = {}
# the "target" folder stores the current folder storing the settings
# the folder is mapped via docker volumes
filepath = f'./target/settings'  
with open(filepath) as fp:  
   line = fp.readline()
   while line:
       data = line.rstrip('\n').split(":",2)
       kv[data[0]] = data[1]
       line = fp.readline()

for k in kv:
    a = a.replace("{{" + k + "}}", kv[k])

print(a)

text_file = open("./target/Output.txt", "w")
text_file.write("a" + a)
text_file.close()

