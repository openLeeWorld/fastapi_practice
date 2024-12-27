from fastapi import FastAPI

app = FastAPI()

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, GenerationConfig
model_name = "google/flan-t5-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
config = GenerationConfig(max_new_tokens=200)
# 모델과 토크나이저는 Hugging Face의 transformers 라이브러리를 통해 로드됩니다.

@app.get("/ai")
def prompt(line: str) -> str:
    tokens = tokenizer(line, return_tensors="pt") # 입력 텍스트를 토큰화
    outputs = model.generate(**tokens, max_new_tokens=config.max_new_tokens) # 모델이 텍스트 생성
    result = tokenizer.batch_decode(outputs, skip_special_tokens=True) # 생성된 토큰을 텍스트로 변환
    return result[0]

# http -b localhost:8000/ai line=="Are cats better than dogs?"
# FastAPI를 사용하여 AI 텍스트 생성 서비스를 제공하는 간단한 웹 API를 구현한 것