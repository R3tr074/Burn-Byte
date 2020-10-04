from bin.addons.arg_manager import arg_manager


def test_arg_manager_empty():
    argv = ["burn"]
    assert arg_manager(argv) == 0


def test_arg_manager_help():
    name = "burn"
    argv = ["-h", "--help", "help"]

    for i in range(0, 3):
        assert arg_manager([name, argv[i]]) == 0


def test_arg_manager_correct():
    argv = ["burn", "--target", "https://google.com",
            "--method", "http", "--time", "10"]

    assert arg_manager(argv) == {
        "threads": 3,
        "target": "https://google.com",
        "time": "10",
        "method": "http",
        "root": True
    }
