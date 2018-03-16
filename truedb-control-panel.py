import os.path, sys, time
from hashlib import sha256
from subprocess import call as cmd

cmd('cls', shell=True)

def hash(string):
    return sha256(string.encode('utf-8')).hexdigest()

def log(text, m=False, mx=0, now=0):
    if m == False:
        print('[TDB] ' + text)
    else:
        print('[TDB] ' + text + ' ('+ str(mx) +'/'+ str(now) +')')

def logi(text, v=''):
    v = input('[TDB] ' + text)
    return v

def slp(sec=''):
    if sec == '':
        time.sleep(0.7)
    else:
        time.sleep(sec)

class trueDatabase(object):
    def __init__(self, dbName):
        self.fileRequest = dbName + '.truedb'
        self.codeRequest = ''
        self.asAble = {}
        self.asUser = ''
    def newFile(self, v='', p='', dbn=''):
        if os.path.isfile(self.fileRequest) == False:
            dbn = logi('Set Database Name: ')
            p = logi('Set Database Password: ')
            v = open(self.fileRequest, 'w')
            v.write('Database=' + dbn + '\nusername=' + hash(dbn) + '\npassword=' + hash(p))
            v.close()
    def readDatabase(self):
        self.codeRequest = open(self.fileRequest, 'r').read().split('\n')
    def checkNewRequest(self, _mx_=3, r={'pass': '', 'user': '', 'passh': '', 'userh': ''}):
        cmd('cls', shell=True)
        log('Please Wait we check something...', True, 0, _mx_)
        if os.path.isfile(self.fileRequest) == True:
            log('Database Exists...', True, 1, _mx_)
        else:
            log('Database Undefinded...', True, 1, _mx_)
            slp()
            sys.exit()
        for l in range(0, len(self.codeRequest)):
            if self.codeRequest[l].split('=')[0] == 'username':
                r['userh'] = self.codeRequest[l].split('=')[1]
        for s in range(0, len(self.codeRequest)):
            if self.codeRequest[s].split('=')[0] == 'password':
                r['passh'] = self.codeRequest[s].split('=')[1]
        r['user'] = logi('-> Login -> Username: ')
        r['pass'] = logi('-> Login -> Password: ')
        if r['user'] != '' and r['pass'] != '':
            if hash(r['user']) == r['userh'] and hash(r['pass']) == r['passh']:
                self.asUser = r['user']
                log('Connected Completed...', True, 2, _mx_)
            else:
                log('Username or Password incorrect...')
                slp()
                sys.exit()
        else:
            log('Something Empty...')
            slp()
            sys.exit()
        if len(self.codeRequest) > 0:
            log('Code Exists... (' + str(len(self.codeRequest)) + ' line(s))', True, 3, _mx_)
        else:
            log('Code Undefinded...', True, 3, _mx_)
            slp()
            sys.exit()
    def setup(self):
        self.newFile()
        self.readDatabase()
        self.checkNewRequest()
        self.getDbData()
        self.main()
    def getDbData(self):
        for unpack in range(0, len(self.codeRequest)):
            try:
                self.asAble[self.codeRequest[unpack].split('=')[0]] = self.codeRequest[unpack].split('=')[1]
            except:
                pass
    def saveDb(self, v=''):
        v = open(self.fileRequest, 'w')
        for wr in range(0, len(self.codeRequest)):
            if self.codeRequest[wr] != '':
                v.write(self.codeRequest[wr] + '\n')
        v.close()
        self.getDbData()
        log('Database Updated...')
    def addData(self, csyntax):
        self.codeRequest.append(csyntax)
        self.saveDb()
    def delData(self, toDel):
        for _del_ in range(0, len(self.codeRequest)):
            if self.codeRequest[_del_].split('=')[0] == toDel:
                del self.codeRequest[_del_]
                break
        self.saveDb()
        log('"' + toDel + '" Deleted from Database...')
    def showDb(self):
        log('<--- Database['+ self.fileRequest +'/'+ self.asUser +'] --->\n')
        print(self.asAble)
        print('\n')
    def get(self, by):
        for search in range(0, len(self.codeRequest)):
            if self.codeRequest[search].split('=')[0] == by:
                return self.codeRequest[search].split('=')[1]
    def update(self, updateThis):
        for update in range(0, len(self.codeRequest)):
            if self.codeRequest[update].split('=')[0] == updateThis.split('=')[0]:
                self.codeRequest[update] = updateThis.split('=')[0] + '=' + updateThis.split('=')[1]
                break
        log('"' + updateThis.split('=')[0] + '" Updated...')
        self.saveDb()
    def query(self, newRequest, v=''):
        v = newRequest.split(':')
        try:
            if v[1].split('=')[0] == 'username' or v[1].split('=')[0] == 'password' or v[1].split('=')[0] == 'database':
                log('You cant change/delete username/password/database. Your access denied and your loged out.')
                slp()
                sys.exit()
        except:
            pass

        if v[0] == 'add':
            self.addData(v[1])
        elif v[0] == 'delete':
            self.delData(v[1])
        elif v[0] == 'show-database':
            self.showDb()
        elif v[0] == 'search':
            log('Result -> ' + self.get(v[1]))
        elif v[0] == 'update':
            self.update(v[1])
        elif v[0] == 'help':
            log('<--- Help[TrueDB] --->\n  > add -> Add New Content to Database -> Syntax: "add:key=value"\n  > delete -> Delete Content from Database -> Syntax: delete:key\n  > show-database -> show all database content\n  > search -> return value by key from database -> Syntax: search:key\n  > update -> update value by key in database -> Syntax: update:key=newvalue\n  > close -> Close database panel')
        elif v[0] == 'close':
            sys.exit()
        else:
            log('Undefinded command...')
        self.main()
    def main(self, command=''):
        command = logi(': ')
        self.query(command)

tdb = ''
def runDb(stringName):
    global tdb
    tdb = trueDatabase(stringName)
    tdb.setup()

fndb = logi('Database File Name (Without ".tdb"): ')
runDb(fndb)
