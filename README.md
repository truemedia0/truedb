# truedb
TrueDatabase is simple and easy database worked with ".tdb" databases and based on Python 3.
Scroll down for full Tutorial in TrueDatabase!

# Updates and news
3/16/2018 -> Upload TrueDatabase to Github. We plan to add socket to project(after it you can get information in another computer from database! :D)

# Tutorial
Welcome new user! download truedatabase and start using right now! very easy and simple database is waiting ;D.

# Tutorial 1 - TrueDatabase_Lib

We have 2 platforms to work with. is truedatabase_lib and truedatabase_control_panel.
Now we learn our lib.

! Everything with an explanation can be found in the lib-example.py file !

We start with importing the lib
```
import truedb_lib # import TrueDatabase Lib
```

After it we need to init TrueDatabase in our project with this code:
```
database = truedb_lib.trueDatabase('here-file-name') # init database
```

We need to use setup before do something with database and fill username and password fields:
```
database.setup({'user': 'choose_username', 'pass': 'choose_password'}) # database setup [first step after init!] +login/register to database
```

Now we start learning functions include lib...

# Tutorial 1.1 - TrueDatabase_Lib -> Functions

Add new data to database:
```
database.addData('key=value') # add new value
```

Add new multiple-data to database:
```
database.addData('key=value1,value2,value3') # multiple values
```

Get(search) data from database:
```
database.get('key') # returned "value"
```

Update keys to new values:
```
database.update('key=updatedvalue') # key updated to "updatedvalue"
```

Delete key from database:
```
database.delData('key') # delete "key" from database
```

Show database output:
```
database.showDb() # Show Database Output [By Request]
```

# Tutorial 1.2 - TrueDatabase_Lib -> Example

We recommend "lib-example.py" to learn our lib...

lib-example.py:
```
import truedb_lib # import TrueDatabase Lib
from random import randint # import randint from random

"""
var.addData('key=value')
var.delData('bykey_to_delete')
var.showDb()
var.get('key')
var.update('key=newvalue')

var = trueDatabase(stringName)
var.setup({'user': 'username', 'pass': 'password'})
"""

database = truedb_lib.trueDatabase('dbfile-example') # init database
database.setup({'user': 'user', 'pass': 'admin'}) # database setup [first step after init!] +login/register to database

database.addData('newvalue'+ str(randint(0,100000)) +'=added') # add newvalue
database.addData('val=wait') # add val
database.get('val') # returned "wait"
database.update('val=updatedvalue') # val updated to "updatedvalue"
database.delData('val') # delete val
database.showDb() # Show Database Output [By Request]

# Example Steps:
# 1) add value named(key) "newvalue" w/ random int seted to value "added"
# 2) add value named(key) "val" seted to value "wait"
# 3) search value by key "val" and return the value "wait"
# 4) change "val" key value to new value "updatedvalue"
# 5) delet "val" key
# 6) print database output after parsing
# ----------------------------------------------------------------------------
# As a result:
# New key + value in database (Example from database document => "newvalue33334=added")
# Output "{'Database': 'user', 'username': '04f8996da763b7a969b1028ee3007569eaf3a635486ddab211d512c85b9df8fb', 'password': '8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918', 'newvalue33334': 'added', 'val': 'updatedvalue'}"
# ! In output we can see "val" and we know he deleted. truedb have include double memory and he save all deleted data. deleted data really deleted 100% when we close truedb(in real time data deleted from dbfile-example.tdb and the key:value only in truedb memory) !
```

# Tutorial 2 - Control Panel
Coming soon...
