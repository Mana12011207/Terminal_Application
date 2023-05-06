import pytest
from counting_to_21game import computer_turn, user_turn
from unittest.mock import patch

#test_user_turn_valid_input tests to ensure that the correct output is returned for a valid input (1 or 2) from the user. 
@pytest.mark.parametrize("input_value, expected_output", [(1, 1), (2, 2)])
def test_user_turn_valid_input(input_value, expected_output):
    with patch('builtins.input', return_value=str(input_value)):
        assert user_turn(5) == expected_output
        

