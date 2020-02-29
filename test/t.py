with open('file.txt', 'r') as file :
  filedata = file.read()

filedata = filedata.replace('funame', 'mum')
filedata = filedata.replace('pass', 'mum')
filedata = filedata.replace('fid', 'mum')
filedata = filedata.replace('cnuser', 'mum')
filedata = filedata.replace('cnip', 'mum')
filedata = filedata.replace('monitport', 'mum')

with open('file.sh', 'w') as file:
  file.write(filedata)







##  "funame"
##  "pass"
## "fid"
## "cnuser"
##"cnip"
##"monitport"
