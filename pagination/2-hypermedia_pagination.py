#!/usr/bin/env python3
"""Madulo donde se calcula la paginacion"""


import csv
import math
from typing import List, Dict, Any
import os


def index_range(page: int, page_size: int):
    """funcion que calcula la paginacion"""
    inicio = ((page - 1) * page_size)
    fin = page * page_size
    return inicio, fin


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Devuelve una página del dataset"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        dataset = self.dataset()

        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """Devuelve metadatos de paginación junto con la página de datos."""
        data = self.get_page(page, page_size)

        total_items = len(self.dataset())
        tot_pages = math.ceil(total_items / page_size) if page_size > 0 else 0

        current_page_size = len(data)

        prev_page = page - 1 if page > 1 else None
        next_page = page + 1 if page < tot_pages else None

        return {
            "page_size": current_page_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": tot_pages,
        }
