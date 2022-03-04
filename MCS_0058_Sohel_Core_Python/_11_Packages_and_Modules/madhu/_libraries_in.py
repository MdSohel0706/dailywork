'''
builtins***
csv***
datetime**
json*** json.dumps() json.loads() pickling/unpickling serialization/deserialization
logging***
pdb*** Debugging
pip***


abc*        : abstract base class used in Abstract Class in OOPs
asyncio*    :
base64**    :
collections* :
copy*
http* - sftp https smtp ftp
importlib
io*
ipaddress
multiprocessing*
os*
pickle*
smtplib
socket
sqlite3
ssl
subprocess
threading*
time*
timeit*
'''

import base64

message = "GeeksForGeeks is the best"
print("Normal message : ", message)
en_message = message.encode("ascii")
print("Encode message : ", en_message)

bs64_msg = base64.b64encode(en_message)
print("Base64 message : ", bs64_msg)

bs64_dec_msg = bs64_msg.decode("ascii")

print(f"Decoded string : {bs64_dec_msg}")