from src.dir_enum import DirectoryEnumerator

def test_directory_list_exists():
    de = DirectoryEnumerator()
    assert isinstance(de.common_paths, list)
    assert "/admin" in de.common_paths
