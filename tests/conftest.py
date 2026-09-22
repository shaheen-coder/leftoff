from pathlib import Path
import pytest

@pytest.fixture
def root_dir() -> Path: return Path('.')
