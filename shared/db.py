import sqlite3
import contextlib
from typing import Any


@contextlib.contextmanager
def get_conn(db_path: str):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def execute(db_path: str, sql: str, params: tuple = ()) -> None:
    with get_conn(db_path) as conn:
        conn.execute(sql, params)


def fetchall(db_path: str, sql: str, params: tuple = ()) -> list[dict]:
    with get_conn(db_path) as conn:
        rows = conn.execute(sql, params).fetchall()
    return [dict(r) for r in rows]


def fetchone(db_path: str, sql: str, params: tuple = ()) -> dict[str, Any] | None:
    with get_conn(db_path) as conn:
        row = conn.execute(sql, params).fetchone()
    return dict(row) if row else None
