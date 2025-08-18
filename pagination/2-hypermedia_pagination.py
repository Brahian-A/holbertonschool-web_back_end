#!/usr/bin/env python3
"""Madulo donde se calcula la paginacion"""


import csv
import math
from typing import List, Dict, Any

class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE, newline="") as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            data = self.dataset()
            self.__indexed_dataset = {i: row for i, row in enumerate(data)}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict[str, Any]:
        """Return deletion-resilient page starting at `index`."""
        assert isinstance(index, int) and index >= 0
        assert isinstance(page_size, int) and page_size > 0

        indexed = self.indexed_dataset()
        if not indexed:
            return {"index": index, "next_index": None, "page_size": 0, "data": []}

        max_idx = max(indexed.keys())
        assert index <= max_idx

        data = []
        current = index
        collected = 0

        while collected < page_size and current <= max_idx:
            item = indexed.get(current)
            if item is not None:
                data.append(item)
                collected += 1
            current += 1

        next_index = current if current <= max_idx else None

        return {
            "index": index,
            "next_index": next_index,
            "page_size": len(data),
            "data": data,
        }

