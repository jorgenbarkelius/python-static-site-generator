#!/usr/bin/env python3

from pathlib import Path


class Site:
    def __init__(self, source, dest):
        self.source = source.Path()
        self.dest = dest.Path()

    def create_dir(self, path):
        directory = self.dest / path.relative_to(self.source)
        directory.mkdir(parents=True, exist_ok=True)

    def build(self):
        self.dest.mkdir(parents=True, exist_ok=True)
        for path in self.source.rglob("*"):
            if path.is_dir():
                self.create_dir(path)
