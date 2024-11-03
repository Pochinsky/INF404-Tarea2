from os import path
from data.instances import generate_single_instance

# generate test instance if not exists
TEST_INSTANCE = {
    "file_path": "./data/test_instance.txt",
    "range_x": 20,
    "range_y": 20,
    "K": 45,
    "L": 40,
}

if not path.isfile(TEST_INSTANCE["file_path"]):
    generate_single_instance(
        TEST_INSTANCE["range_x"],
        TEST_INSTANCE["range_y"],
        TEST_INSTANCE["K"],
        TEST_INSTANCE["L"],
        TEST_INSTANCE["file_path"],
    )
