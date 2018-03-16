import os.path, sys, time
from hashlib import sha256
def hash(string):
    return sha256(string.encode('utf-8')).hexdigest()
class trueDatabase(object):
    def __init__(self, dbName):
        self.fileRequest = dbName + '.truedb'
        self.codeRequest = ''
        self.asAble = {}
        self.asUser = ''
    def newFile(self, p='', dbn='', v=''):
        if os.path.isfile(self.fileRequest) == False:
            v = open(self.fileRequest, 'w')
            v.write('Database=' + dbn + '\nusername=' + hash(dbn) + '\npassword=' + hash(p))
            v.close()
    def readDatabase(self):
        self.codeRequest = open(self.fileRequest, 'r').read().split('\n')
    def checkNewRequest(self, login={'username': '', 'password': ''}, r={'pass': '', 'user': '', 'passh': '', 'userh': ''}):
        if os.path.isfile(self.fileRequest) == True:
            pass
        else:
            log('Database Undefinded...')
            slp()
            sys.exit()
        for l in range(0, len(self.codeRequest)):
            if self.codeRequest[l].split('=')[0] == 'username':
                r['userh'] = self.codeRequest[l].split('=')[1]
        for s in range(0, len(self.codeRequest)):
            if self.codeRequest[s].split('=')[0] == 'password':
                r['passh'] = self.codeRequest[s].split('=')[1]
        r['user'], r['pass'] = login['username'], login['password']
        if r['user'] != '' and r['pass'] != '':
            if hash(r['user']) == r['userh'] and hash(r['pass']) == r['passh']:
                self.asUser = r['user']
            else:
                sys.exit()
        else:
            sys.exit()
        if len(self.codeRequest) > 0:
            pass
        else:
            sys.exit()
    def setup(self, newfileData={'user': '', 'pass': ''}):
        self.newFile(newfileData['pass'], newfileData['user'])
        self.readDatabase()
        self.checkNewRequest({'username': newfileData['user'], 'password': newfileData['pass']})
        self.getDbData()
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
    def addData(self, csyntax):
        self.codeRequest.append(csyntax)
        self.saveDb()
    def delData(self, toDel):
        for _del_ in range(0, len(self.codeRequest)):
            if self.codeRequest[_del_].split('=')[0] == toDel:
                del self.codeRequest[_del_]
                break
        self.saveDb()
    def showDb(self):
        print(self.asAble)
    def get(self, by):
        for search in range(0, len(self.codeRequest)):
            if self.codeRequest[search].split('=')[0] == by:
                return self.codeRequest[search].split('=')[1]
    def update(self, updateThis):
        for update in range(0, len(self.codeRequest)):
            if self.codeRequest[update].split('=')[0] == updateThis.split('=')[0]:
                self.codeRequest[update] = updateThis.split('=')[0] + '=' + updateThis.split('=')[1]
                break
        self.saveDb()

"""
var.addData('key=value')
var.delData('bykey_to_delete')
var.showDb()
var.get('key')
var.update('key=newvalue')

var = trueDatabase(stringName)
var.setup({'user': 'username', 'pass': 'password'})
"""
