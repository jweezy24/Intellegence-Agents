import json
import yaml
import os
import subprocess
import os
import psycopg2

#DATABASE_URL = os.environ['DATABASE_URL']

class cacheTable:
    def __init__(self, user, hash, vals):
        sql = """CREATE TEMP TABLE {0}(id SERIAL PRIMARY KEY, title VARCHAR(64),
        note VARCHAR(64), tags VARCHAR(64), summary VARCHAR(64), url VARCHAR(64), active BOOLEAN);"""
        sql = sql.format(hash)
        self.user = user
        self.hash = hash
        self.conn = psycopg2.connect(host='localhost',database='testing', user='postgres', password='Jkop4678!@')
        self.cursor = self.conn.cursor()
        self.cursor.execute(sql)
        self.conn.commit()
        for row in vals:
            self.add_zet(row)

    def add_zet(self, val):
        sql = """INSERT INTO {0}(title, note, tags, summary, url, active)
                 VALUES('{1}','{2}','{3}','{4}','{5}','{6}');"""
        sql = sql.format(self.hash, val[0], val[1], val[2], val[3], val[4], val[5])
        self.cursor.execute(sql)
        self.conn.commit()

    def get_zets(self):
        sql = """SELECT * FROM {0};"""
        sql = sql.format(self.hash)
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def __del__(self):
        self.conn.close()
