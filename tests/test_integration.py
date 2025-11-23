import subprocess

def test_hello_integration():
    # Integration test: run the program as a script
    result = subprocess.run(
        ["python", "hello.py"],
        capture_output=True,
        text=True
    )
    # Check that the script prints the expected output
    assert result.stdout.strip() == "Hello, World!"
