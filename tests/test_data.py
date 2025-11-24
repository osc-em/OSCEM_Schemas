"""Data test."""
import os
import glob
import unittest

from linkml_runtime.loaders import yaml_loader
from oscem_schemas.datamodel.oscem_schemas import EMDataset

ROOT = os.path.join(os.path.dirname(__file__), '..')
DATA_DIR = os.path.join(ROOT, "test", "data", "examples")

EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR, '*.yaml')) + glob.glob(os.path.join(DATA_DIR, '*.json'))


class TestData(unittest.TestCase):
    """Test data and datamodel."""

    def test_data(self):
        """Data test."""
        for path in EXAMPLE_FILES:
            obj = yaml_loader.load(path, target_class=EMDataset)
            assert obj
