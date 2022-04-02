from abc import ABC, abstractmethod
from libqtile.config import Key
from typing import List
from libqtile.lazy import lazy
from pydantic import BaseModel
from juselara_qtile.dataclasses import Keys

class KeyLoader(ABC):
    keys: List[Key]

    @abstractmethod
    def load(self, kind: str, keys: List[str]):
        ...

    @abstractmethod
    def extract(self) -> List[Key]:
        ...

class KeyLoaderImpl(KeyLoader):
    def __init__(self):
        self.keys = []

    @abstractmethod
    def load(self, kind: str, keys: List[str]):
        ...

    def extract(self) -> List[Key]:
        return self.keys

class SingleKeyLoader(KeyLoaderImpl):
    def load(self, kind: str, keys: List[str]):
        func = eval(f"lazy.layout.{kind}")
        self.keys.append(Key([keys[0]], keys[1], func()))

class DoubleKeyLoader(KeyLoaderImpl):
    def load(self, kind: str, keys: List[str]):
        func = eval(f"lazy.layout.{kind}")
        self.keys.append(Key([keys[0], keys[1]], keys[2], func()))

class StopKeyLoader(KeyLoaderImpl):
    def load(self, kind: str, keys: List[str]):
        func = eval(f"lazy.{kind}")
        self.keys.append(Key([keys[0], keys[1]], keys[2], func()))

class KeySpawnLoader(KeyLoaderImpl):
    def load(self, kind: str, keys: List[str]):
        func = lazy.spawn(kind)
        self.keys.append(Key([keys[0]], keys[1], func()))

class UtilsKeyLoader(KeyLoaderImpl):
    funcs = {
            "normalize": lazy.layout.normalize,
            "maximize": lazy.layout.maximize,
            "next_screen": lazy.screen.next,
            "quit": lazy.shutdown,
            "restart": lazy.restart,
            "shutdown": lazy.shutdown
            }

    def load(self, kind: str, keys: List[str]):
        func = self.funcs[kind]
        self.keys.append(Key([keys[0]], keys[1], func()))

class CustomKeyLoader(KeyLoaderImpl):
    def load(self, kind: str, keys: List[str]):
        func = lazy.spawn(kind)
        self.keys.append(Key([keys[0]], keys[1], func))

class KeyManager:
    def __init__(self, input_keys: Keys):
        self.input_keys = input_keys
        self.output_keys: List[Key] = []

    def load_keys(self, keys: BaseModel, loader: KeyLoader):
        print(keys)
        for kind in keys.dict().keys():
            element = getattr(keys, kind)
            loader.load(kind, element)
        self.output_keys.extend(loader.extract())

    def __call__(self) -> List[Key]:
        self.output_keys = []
        self.load_keys(self.input_keys.switch, SingleKeyLoader())
        self.load_keys(self.input_keys.move, DoubleKeyLoader())
        self.load_keys(self.input_keys.resize, DoubleKeyLoader())
        self.load_keys(self.input_keys.utils, UtilsKeyLoader())
        self.load_keys(self.input_keys.custom, CustomKeyLoader())
        self.load_keys(self.input_keys.stop, StopKeyLoader())
        return self.output_keys
