#!/usr/bin/env bash

sqlite3 store.db "CREATE TABLE IF NOT EXISTS $1 ($2)"
sqlite3 store.db ".import /dev/stdin $1"
