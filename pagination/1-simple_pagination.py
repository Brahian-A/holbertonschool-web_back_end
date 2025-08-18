#!/usr/bin/env python3
"""Madulo donde se calcula la paginacion"""


import csv
import math
from typing import List
import os

def index_range(page: int, page_size: int):
    """funcion que calcula la paginacion"""
    inicio = ((page - 1) * page_size)
    fin = page * page_size
    return inicio, fin


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = os.path.join(os.path.dirname(__file__), "Popular_Baby_Names.csv")

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
