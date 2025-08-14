#!/usr/bin/env python3

def index_range(page: int, page_size: int):
    inicio = ((page - 1) * page_size)
    fin = page * page_size
    return inicio, fin
