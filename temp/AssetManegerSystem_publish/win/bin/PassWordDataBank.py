import os
import script
import sqlite3

class PassWordDataBank():
    initPath = ''
    dataBasePath = ''

    def __init__(self):
        self.initPath = script.getAssetManagerPath()['main']
        self.dataBasePath = self.initPath + '\\data\\user_data.db'

    def val(self, name, pw):
        data = self.showdate(name)
        if data:
            passworld = pw
            if data[2] == passworld:
                print "pass word confirm"
                return True
            else:
                print"pass word refuse"
                return False
        else:
            print"pass word empty"
            return False

    def showdate(self, username):
        sql = self.bankInit()
        data = sql.execute("select * from user where name='%s'" % username).fetchone()
        sql.close()
        return data

    def bankInit(self):
        dataExt = os.path.exists(self.dataBasePath)
        sql = ''
        if not dataExt:
            sql = sqlite3.connect(self.dataBasePath)
            sql.execute(
                """create table if not exists
                %s(
                %s integer primary key autoincrement,
                %s varchar(128),
                %s varchar(128))"""
                % ('user',
                   'id',
                   'name',
                   'passworld'))
            sql.close()
        else:
            sql = sqlite3.connect(self.dataBasePath)

        return sql

    def register(self, input_name, input_passworld):
        sql = self.bankInit()
        data = sql.execute("select * from user where name='%s'" % input_name).fetchone()
        if not data:
            sql.execute("insert into user(name,passworld) values(?,?)",
                        (input_name, input_passworld))
            sql.commit()
            cmds.warning("create user success")
            sql.close()
        else:
            cmds.warning("user already exsits")