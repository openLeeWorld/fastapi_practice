import data.game as data

def get_word() -> str: # 초기화
    return data.get_word()

"""
점수 계산: 점수는 추측한 문자가 올바른 위치에서 일치하는지, 다른 위치에서 일치하는지
아니면 틀렸는지를 나타내는 단일 문자로 된 문자열이다. 
추측한 이름과 정답은 모두 소문자로 변환돼 대소문자를 구분하지 않고 비교한다.
추측한 단어의 길이가 숨겨진 단어와 같지 않으면 점수는 빈 문자열로 반환된다.
"""
from collections import Counter, defaultdict

HIT = "H"
MISS = "M"
CLOSE = "C" # 문자가 맞지만 위치가 틀림
ERROR = ""

def get_score(actual: str, guess: str) -> str:
    length: int = len(actual)
    if len(guess) != length:
        return ERROR
    actual_counter = Counter(actual) # {letter: count, ...}
    guess_counter = defaultdict(int)
    result = [MISS] * length
    for pos, letter in enumerate(guess):
        if letter == actual[pos]:
            result[pos] = HIT
            guess_counter[letter] += 1
    for pos, letter in enumerate(guess):
        if result[pos] == HIT:
            continue
        guess_counter[letter] += 1
        if (letter in actual and 
            guess_counter[letter] <= actual_counter[letter]):
            result[pos] = CLOSE
    result = ''.join(result)
    return result