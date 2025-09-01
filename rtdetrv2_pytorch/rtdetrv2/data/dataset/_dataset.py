"""Copyright(c) 2023 lyuwenyu. All Rights Reserved."""

import torch.utils.data as data


class DetDataset(data.Dataset):
    def __getitem__(self, index):
        img, target = self.load_item(index)
        if self.transforms is not None:
            img, target, _ = self.transforms(img, target, self)
        return img, target

    def load_item(self, index):
        raise NotImplementedError(
            "Please implement this function to return item before `transforms`."
        )

    def set_epoch(self, epoch) -> None:
        self._epoch = epoch

    @property
    def epoch(self):
        return self._epoch if hasattr(self, "_epoch") else -1

    @property
    def categories(
        self,
    ):
        return None

    @property
    def category2name(
        self,
    ):
        return None

    @property
    def category2label(
        self,
    ):
        return None

    @property
    def label2category(
        self,
    ):
        return None
