import sys
import ast
import os
from os import path

def AddUser(user, password):
  user_list = []
  #print(os.stat("users.txt").st_size == 0)
  if not (os.stat("users.txt").st_size == 0): #If not empty file
    with open('users.txt', 'r') as f:  # Getting contents of file
      user_list = ast.literal_eval(f.read())
  
  #print("user list: "+ str(user_list))
  if ([username for username in user_list if username[0] == user]): # If username already exists
    print("Error: user exists")
    return
  
  user_list.append((user,password))
  with open("users.txt", "w") as output:
    output.write(str(user_list))
  print("Success")
  return

def Authenticate(user, password):
  user_list = []
  #print(os.stat("users.txt").st_size == 0)
  if not (os.stat("users.txt").st_size == 0): #If not empty file
    with open('users.txt', 'r') as f:  # Getting contents of file
      user_list = ast.literal_eval(f.read())
  
  #print("user list: "+ str(user_list))
  if (len(user_list) == 0): # If user list is empty 
    print("Error: no such user")
    return
  
  for username in user_list:
    if (username[0] == user and username[1] != password): # Found username, but password is incorrect
      print("Error: bad password")
      return
    elif(username[0] == user and username[1] == password ): # Correct username and password found
      print("Success")
      return
    
  print("Error: no such user") # Could not find user, thus does not exist
  return

def SetDomain(user, domain, flag = 0):
  user_list = []
  if not (os.stat("users.txt").st_size == 0): # If not empty file
    with open('users.txt', 'r') as f:  # Getting contents of file
      user_list = ast.literal_eval(f.read())
  
  #print("user list: "+ str(user_list))
  if (len(user_list) == 0 and flag == 0): # If user list is empty 
    print("Error: no such user")
    return
  
  if (flag == 1): 
        checkDomain(user,domain,1)
        return
  
  for username in user_list:
    if (username[0] == user): # User exists
        checkDomain(user,domain) # Applying user to domain
        return
  
  print("Error: no such user") # Could not find user, thus does not exist
  
  return

def checkDomain(user,domain,flag = 0):
  domain_list = []
  if not (os.stat("domains.txt").st_size == 0): #If not empty file
    with open('domains.txt', 'r') as f:  # Getting contents of file
      domain_list = ast.literal_eval(f.read())
  
  #print("domain list: "+ str(domain_list))
  for d in domain_list:
    if (domain == d[1]):
      if (user == d[0]):
        print("Error: user exists")
        return

  domain_list.append((user,domain)) # appending to domain_list
  with open("domains.txt", "w") as output:
    output.write(str(domain_list))
  if (flag == 1):
    return
  print("Success")
  return

def DomainInfo(domain):
  domain_list = []
  if not (os.stat("domains.txt").st_size == 0): #If not empty file
    with open('domains.txt', 'r') as f:  # Getting contents of file
      domain_list = ast.literal_eval(f.read())
  
  #print("domain list: "+ str(domain_list))
  
  for d in domain_list:
    if (d[1] == domain):
      if (not (d[0])):
        continue
      else:
        print(str(d[0]))

  return

def SetType(objectName, type_name, flag = 0):
  type_list = []
  if not (os.stat("types.txt").st_size == 0): #If not empty file
    with open('types.txt', 'r') as f:  # Getting contents of file
      type_list = ast.literal_eval(f.read())
  
  #print("type list: "+ str(type_list))
  for t in type_list:
    if (type_name == t[1]):
      if (objectName == t[0]):
        print("Error: object already exists")
        return
  
  type_list.append((objectName,type_name)) # appending to type_list
  
  with open("types.txt", "w") as output:
    output.write(str(type_list))
  
  if (flag == 1):
    return
  print("Success")
  
  return


def TypeInfo(type_name):
  type_list = []
  if not (os.stat("types.txt").st_size == 0): #If not empty file
    with open('types.txt', 'r') as f:  # Getting contents of file
      type_list = ast.literal_eval(f.read())
  
  #print("type list: "+ str(type_list))
  
  for t in type_list:
    if (t[1] == type_name):
      if (not (t[0])):
        continue
      else:
        print(str(t[0]))
  return


def AddAccess(operation, domain_name, type_name):
  ap_list = []
  if not (os.stat("ap.txt").st_size == 0): # If not empty file
    with open('ap.txt', 'r') as f:  # Getting contents of file
      ap_list = ast.literal_eval(f.read())
  
  #print("ap list: "+ str(ap_list))
  if not (os.stat("domains.txt").st_size == 0): #If not empty file
    with open('domains.txt', 'r') as f:  # Getting contents of file
      domain_list = ast.literal_eval(f.read())
  
  dflag = 0
  for d in domain_list:
    if (domain_name == d[1]):
      dflag = 1
      break

  if (dflag == 0):
    SetDomain("",domain_name,1)
  
  if not (os.stat("types.txt").st_size == 0): #If not empty file
    with open('types.txt', 'r') as f:  # Getting contents of file
      type_list = ast.literal_eval(f.read())

  tflag = 0
  for t in type_list:
    if (type_name == t[1]):
      tflag = 1
      break

  if (tflag == 0):
    SetType("",type_name,1)
  
  ap_list.append((operation,domain_name,type_name)) # appending to ap_list
  with open("ap.txt", "w") as output:
    output.write(str(ap_list))
  
  print("Success")
  return


def CanAccess(operation, user, obj):
  # Get domains for user
  domain_list = []
  user_domains = []
  if not (os.stat("domains.txt").st_size == 0): #If not empty file
    with open('domains.txt', 'r') as f:  # Getting contents of file
      domain_list = ast.literal_eval(f.read())
  
  #print("domain list: "+ str(domain_list))

  for d in domain_list:
    if (d[0] == user):
      user_domains.append(d[1])
  #print("user domains: "+ str(user_domains))
  # Get types for object
  type_list = []
  object_types = []
  if not (os.stat("types.txt").st_size == 0): #If not empty file
    with open('types.txt', 'r') as f:  # Getting contents of file
      type_list = ast.literal_eval(f.read())
  
  #print("type list: "+ str(type_list))
  
  for t in type_list:
    if (t[0] == obj):
      object_types.append(t[1])
  #print("types for object: "+ str(object_types))
  
  # Get access permissions list
  ap_list = []
  access_list = []
  if not (os.stat("ap.txt").st_size == 0): # If not empty file
    with open('ap.txt', 'r') as f:  # Getting contents of file
      ap_list = ast.literal_eval(f.read())
  
  #print("ap list: "+ str(ap_list))
  
  # If access control list contains operation get the domain and type
  for ap in ap_list:
    if (ap[0] == operation):
      access_list.append((ap[1],ap[2]))
  #print("(domain,type) pairs for operation: "+ str(access_list))
  
  # Psuedocode logic implementation
  for d in user_domains:
    for t in object_types:
      if (d,t) in access_list:
        print("Success")
        return
  
  print("Error: access denied")
  return

#print (str(sys.argv))

if (not path.exists("users.txt")):
  f = open("users.txt","w+")
  f.close()

if (not path.exists("domains.txt")):
  f = open("domains.txt","w+")
  f.close()

if (not path.exists("types.txt")):
  f = open("types.txt","w+")
  f.close()

if (not path.exists("ap.txt")):
  f = open("ap.txt","w+")
  f.close()

operation = sys.argv
cmd = str(sys.argv[1])

if cmd == "AddUser":
  #print(cmd)
  if (len(sys.argv) != 4):
    print("Error: wrong number of arguments")
  else:
    if (not (sys.argv[2])): #Handles case of username is missing or empty string
      print("Error: username missing")
    else:
      AddUser(str(sys.argv[2]),str(sys.argv[3]))

elif (cmd == "Authenticate"):
  if (len(sys.argv) != 4): 
    print("Error: wrong number of arguments")
  else:
    Authenticate(str(sys.argv[2]),str(sys.argv[3]))
elif (cmd == "SetDomain"):
  if (len(sys.argv) != 4 or not (sys.argv[3]) ): #Handles case of domain name is missing or empty string
    print("Error: missing domain")
  else:
    SetDomain(str(sys.argv[2]),str(sys.argv[3]))
elif (cmd == "DomainInfo"):
  if (len(sys.argv) != 3): 
    print("Error: wrong number of arguments")
  else:  
    if (not (sys.argv[2]) ): #Handles case of domain name is missing or empty string
      print("Error: missing domain")
    else:
      DomainInfo(str(sys.argv[2]))
elif (cmd == "SetType"):
  if (len(sys.argv) != 4 or (not (sys.argv[2])) or (not (sys.argv[3]))): #Handles case of object or type_name is missing or empty string
    print("Error: object or type name missing")
  else:
    SetType(str(sys.argv[2]),str(sys.argv[3]))
elif (cmd == "TypeInfo"):
  if (len(sys.argv) != 3): 
    print("Error: wrong number of arguments")
  else:
    if (not (sys.argv[2]) ): #Handles case of type_name is missing or empty string
      print("Error: missing type name")
    else:
      TypeInfo(str(sys.argv[2]))
elif (cmd == "AddAccess"):
  flag = 0 # Flag that helps determine whether a parameter is null
  tf = 0 # Try-except flag that helps determine whether a parameter is null
  if (len(sys.argv) != 5): #Handles case of username is missing or empty string
    print("Error: wrong number of arguments")
    flag = 1
  try:
    op = (sys.argv[2])
  except:
    print("Error: missing operation")
    tf = 1
  try:
    d = (sys.argv[3])
  except:
    print("Error: missing domain")
    tf = 1
  try:
    t = (sys.argv[4])
  except:
    print("Error: missing type")
    tf = 1
  
  if (tf != 1):
    if ((not (sys.argv[2])) ): #Checking if operation is null
      flag = 1
      print("Error: missing operation")
    if (((not (sys.argv[3])) )): #Checking if domain is null
      flag = 1
      print("Error: missing domain")
    if((not (sys.argv[4])) ): #Checking if type is null
      flag = 1
      print("Error: missing type")
    if (flag == 0): # All parameters present
      AddAccess(str(sys.argv[2]),str(sys.argv[3]),str(sys.argv[4]))

elif (cmd == "CanAccess"):
  if (len(sys.argv) != 5): #Handles case of username is missing or empty string
    print("Error: wrong number of arguments")
  else:
    CanAccess(str(sys.argv[2]),str(sys.argv[3]),str(sys.argv[4]))
  

        
    
  
