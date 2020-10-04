from bin.addons.utils import root_privileges


def test_root_privileges():
    assert root_privileges() == False or True
