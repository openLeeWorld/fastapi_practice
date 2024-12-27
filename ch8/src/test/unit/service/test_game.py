import pytest
from service import game

word = "bigfoot"
guesses = [
    ("bigfoot", "HHHHHHH"),
    ("abcdefg", "MCMMMCC"),
    ("toofgib", "CCCHCCC"),
    ("wronglength", ""),
    ("", ""),
]

"""
테스트 함수에 여러 가지 입력 값을 전달하여 반복적으로 테스트를 실행할 수 있게 합니다. 
이를 통해 동일한 테스트 함수에 대해 다양한 입력 값과 기대 결과를 쉽게 테스트할 수 있습니다.
"""
@pytest.mark.parametrize("guess,score", guesses)
def test_match(guess, score):
    assert game.get_score(word, guess) == score
