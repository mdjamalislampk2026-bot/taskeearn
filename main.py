# ============================================================
# TASK EARN - SINGLE FILE ANDROID MVP
# Python + Kivy + KivyMD + SQLite
# ============================================================

import sqlite3
import hashlib
import secrets
from datetime import datetime, date

from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivy.uix.screenmanager import Screen

from kivymd.app import MDApp


# ============================================================
# DATABASE
# ============================================================

DB = "taskeearn.db"


def connect():
    return sqlite3.connect(DB)


def hash_password(password):
    return hashlib.sha256(
        password.encode("utf-8")
    ).hexdigest()


def init_database():

    con = connect()
    cur = con.cursor()

    # USERS
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            passwor
