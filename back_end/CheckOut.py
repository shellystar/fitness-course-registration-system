# -*- coding: utf-8 -*-
import pyodbc

def checkout(conn):
    if conn:
        conn.close()
    return 0