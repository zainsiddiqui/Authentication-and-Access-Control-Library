# Description
This program comprises of an authentication and access control (authorization) library in Python which can be used by services that need to rely on their own set of users rather than those who have accounts on the computer.

# Created by
Zain Siddiqui

## Installation
No installation required, program only uses built in libraries (sys,ast,os) in python. There is no reliance on any IDE or third-party libraries.

## Running Program
Use the portal.py file to run the python program and specify respective commands.

```
$ python portal.py [command] [param1] [param2]...
```

## Example of various test scripts
```
$ python portal.py AddUser alice monkey
Success
```

```
$ python portal.py Authenticate alice monkey
Success
```

```
python portal.py Authenticate alice password
Error: bad password
```

```
python portal.py SetDomain alice admin
Success
```

```
python portal.py SetDomain abvfd ""
Error: missing domain
```

```
python portal.py DomainInfo admin
alice
```

```
python portal.py DomainInfo ""
Error: missing domain
```

```
python portal.py SetType mulan.mp4 videos
Success
```

```
python portal.py SetType "" movies
Error: object or type name missing
```

```
python portal.py SetType Madagascar ""
Error: object or type name missing
```

```
python portal.py TypeInfo videos
mulan.mp4
```

```
python portal.py TypeInfo ""
Error: missing type name
```

```
python portal.py AddAccess download Editor Videos
Success
```

```
python portal.py CanAccess download alice mulan.mp4
Success
```

```
python portal.py CanAccess cats dogs users
Error: access denied
```