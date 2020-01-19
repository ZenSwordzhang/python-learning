#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

import psycopg2


def get_conn():
    my_db = {
        'user': 'postgres',
        'port': 5432,
        'host': '127.0.0.1',
        'password': '1234',
        'database': 'my_db'}
    return psycopg2.connect(**my_db)


class TestConnectionPostgres(unittest.TestCase):

    def test_create1(self):
        conn = get_conn()
        cur = conn.cursor()
        cur.execute('CREATE TABLE python.test1 (id serial PRIMARY KEY, num integer, data varchar);')
        conn.commit()
        cur.close()
        conn.close()

    def test_create2(self):
        conn = psycopg2.connect(host="127.0.0.1", user="postgres", password="1234", database="my_db", port=5432)
        cur = conn.cursor()
        cur.execute('CREATE TABLE python.test1 (id serial PRIMARY KEY, num integer, data varchar);')
        conn.commit()
        cur.close()
        conn.close()


if __name__ == '__main__':
    unittest.main()
