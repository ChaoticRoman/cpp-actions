import os
import subprocess
import json

repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
binary_path = os.path.join(repo_root, "pretty-json")
example_path = os.path.join(repo_root, "example.json")

print(example_path)

def test_pretty_json_output():
    result = subprocess.run([binary_path, example_path], capture_output=True, text=True, check=True)

    output = result.stdout
    expected = json.dumps(
        ["Hello", 1, True, {"another_key": 666, "key": "value"}],
        indent=4
    )

    assert output == expected, f"Expected output:\n{expected}\n\nGot:\n{output}"


if __name__ == "__main__":
    from pytest import main
    main()
