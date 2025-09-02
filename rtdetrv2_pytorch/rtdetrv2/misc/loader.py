import importlib


def import_modules(modules: list[str]):
    for module in modules:
        importlib.import_module(module)
