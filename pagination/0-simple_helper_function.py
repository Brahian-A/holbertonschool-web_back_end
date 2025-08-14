#!/usr/bin/env python3
"""Madulo donde se calcula la paginacion"""


def index_range(page: int, page_size: int):
    """funcion que calcula la paginacion"""
    inicio = ((page - 1) * page_size)
    fin = page * page_size
    return inicio, fin
