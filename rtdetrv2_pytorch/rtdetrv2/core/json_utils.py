import json
import os

__all__ = ["dump_config"]


def dump_config(cfg, file_path):
    _, ext = os.path.splitext(file_path)
    assert ext in [".json"], "only support json files"

    with open(file_path, "w") as f:
        json.dump(cfg, f, indent=4)
