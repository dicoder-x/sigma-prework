# Test Driven Development TDD

# Basic setup

- Create a venv: python3 -m venv .venv
- activate venv: source .venv/bin/activate
- Install requirements: pip3 install -r requirements.txt
- Check installations: pip3 list

### TDD

- Figure out what you want to do
    - Write function signature {
        def is_valid_square(sides: list[int]) -> bool:
            """Returns True if sides form a valid square"""
    }
    - Identify scenarios for the function
- Write tests that would pass if you had done it
- Check that the tests fail (RED)
- Write code to make the tests pass (GREEN)
- Go back to the start & improve code (REFACTOR)

Possible scenarios:
- Valid input, return True
    - [1, 1, 1, 1]
- Valid input, return False
    - [1, 2, 3, 4]
    - [2, 2, 2]
- Invalid input