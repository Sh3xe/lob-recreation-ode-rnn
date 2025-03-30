import pandas as pd
from torch.utils.data import Dataset
import torch

class OrderBookDataset(Dataset):
    def __init__(self, order_book_path: str, message_path: str, history_size: int):
        """
            order_book_path: path to the csv containing the levels of order_book
            message_path: path to the csv containing past trades
            history_size: number of past trades considerated when getting an item
        """

        lob_names = [(a+str(i)) for i in range(5) for a in ["ap", "as", "bp", "bs"]]
        self.order_book = pd.read_csv(
            order_book_path,
            names = lob_names
        )

        trade_names = ["time", "type", "order_id", "size", "price", "direction"]
        self.trades = pd.read_csv(
            message_path,
            names = trade_names
        )

        assert self.trades.shape[0] == self.order_book.shape[0]

        self.history_size = history_size

    def __getitem__(self, index):
        return super().__getitem__(index)
    
    def __len__(self):
        return self.trades.shape[0]