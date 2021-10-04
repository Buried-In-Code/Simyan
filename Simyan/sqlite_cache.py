"""
SQLite Cache module.

This module provides the following classes:

- SqliteCache
"""
import json
import sqlite3
from datetime import datetime, timedelta
from typing import Any, Dict, Optional


class SqliteCache:
    """
    The SqliteCache object to cache search results from ComicVine.

    Args:
        name: Path and database name to use.
        expiry: How long to keep cache results.

    Attributes:
        expiry (int, Optional): How long to keep cache results.
        con (Connection): Database connection
        cur (Cursor): Database cursor
    """

    def __init__(self, name: str = "Simyan-Cache.sqlite", expiry: Optional[int] = 14):
        self.expiry = expiry
        self.con = sqlite3.connect(name)
        self.cur = self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS queries (query, response, expiry);")
        self.delete()

    def select(self, query: str) -> Dict[str, Any]:
        """
        Retrieve data from the cache database.

        Args:
            query: Search string

        Returns:
            Dict with select result or empty
        """
        if self.expiry:
            self.cur.execute(
                "SELECT response FROM queries WHERE query = ? AND expiry > ?;",
                (query, datetime.now().strftime("%Y-%m-%d")),
            )
        else:
            self.cur.execute(
                "SELECT response FROM queries WHERE query = ?;",
                (query,),
            )
        result = self.cur.fetchone()
        if result:
            return json.loads(result[0])
        return {}

    def get(self, key: str) -> Optional[Dict[str, Any]]:
        """
        Retrieve data from the cache database.

        Args:
            key: Search string

        Returns:
            Dict with select result or empty
        """
        return self.select(query=key) or None

    def insert(self, query: str, response: str):
        """
        Insert data into the cache database.

        Args:
            query: Search string
            response: data to save
        """
        if self.expiry:
            expiry = datetime.now() + timedelta(days=self.expiry)
        else:
            expiry = datetime.now()
        self.cur.execute(
            "INSERT INTO queries(query, response, expiry) VALUES(?, ?, ?);",
            (query, json.dumps(response), expiry.strftime("%Y-%m-%d")),
        )
        self.con.commit()

    def store(self, key: str, value: str):
        """
        Insert data into the cache database.

        Args:
            key: Search string
            value: data to save
        """
        return self.insert(query=key, response=value)

    def delete(self):
        """Remove all expired data from the cache database."""
        if not self.expiry:
            return
        self.cur.execute(
            "DELETE FROM queries WHERE expiry < ?;",
            (datetime.now().strftime("%Y-%m-%d"),),
        )
        self.con.commit()
