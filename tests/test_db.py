import os
import sys
import sqlite3
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


def test_shared_db_execute_and_fetch(tmp_path):
    from shared import db
    test_db = str(tmp_path / "test.db")
    db.execute(test_db, "CREATE TABLE items (id INTEGER PRIMARY KEY, name TEXT)")
    db.execute(test_db, "INSERT INTO items (name) VALUES (?)", ("hello",))
    rows = db.fetchall(test_db, "SELECT * FROM items")
    assert len(rows) == 1
    assert rows[0]["name"] == "hello"


def test_fetchone_returns_none_when_missing(tmp_path):
    from shared import db
    test_db = str(tmp_path / "test2.db")
    db.execute(test_db, "CREATE TABLE items (id INTEGER PRIMARY KEY, name TEXT)")
    row = db.fetchone(test_db, "SELECT * FROM items WHERE id = 999")
    assert row is None
