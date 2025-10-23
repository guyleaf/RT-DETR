import importlib
import importlib.util
import os
import sys


def import_modules(modules: list[str]):
    for module in modules:
        importlib.import_module(module)


# from https://stackoverflow.com/questions/67631/how-to-import-a-module-given-the-full-path
def _import_file(module_name, file_path, make_importable=False):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    if make_importable:
        sys.modules[module_name] = module
    return module


_ENV_SETUP_DONE = False


def setup_environment():
    """Perform environment setup work. The default setup is a no-op, but this
    function allows the user to specify a Python source file or a module in
    the $RTDETRV2_ENV_MODULE environment variable, that performs
    custom setup work that may be necessary to their computing environment.

    Modified from detectron2.uilts.env
    Copyright (c) Facebook, Inc. and its affiliates.
    """
    global _ENV_SETUP_DONE
    if _ENV_SETUP_DONE:
        return
    _ENV_SETUP_DONE = True

    custom_module_path = os.environ.get("RTDETRV2_ENV_MODULE")

    if custom_module_path:
        setup_custom_environment(custom_module_path)
    else:
        # The default setup is a no-op
        pass


def setup_custom_environment(custom_module):
    """
    Load custom environment setup by importing a Python source file or a
    module, and run the setup function.

    Modified from detectron2.uilts.env
    Copyright (c) Facebook, Inc. and its affiliates.
    """
    if custom_module.endswith(".py"):
        module = _import_file("rtdetrv2.misc.env.custom_module", custom_module)
    else:
        module = importlib.import_module(custom_module)
    assert hasattr(module, "setup_environment") and callable(
        module.setup_environment
    ), (
        "Custom environment module defined in {} does not have the "
        "required callable attribute 'setup_environment'."
    ).format(custom_module)
    module.setup_environment()
