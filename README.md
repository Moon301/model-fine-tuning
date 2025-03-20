# model-fine-tuning

## 파인튜닝 준비 단계
1. csv 데이터
    ev 원본데이터를 종류별로 label을 붙이기 

## 모델준비
1. csv 데이터플 다루려면 "테이블 데이터(TABULAR DATA)"를 학습할 수 있는 방법이 필요
2. 모델은 보통 텍스트 기반이라, csv 데이터를 문자열로 변환하는 과정 필요

## 설치 라이브러리
``` bash
pip install transformers datasets pandas torch scikit-learn
```
transformers → Hugging Face에서 제공하는 사전학습된 모델 사용
datasets → Hugging Face에서 데이터셋을 쉽게 불러오고 사용할 수 있도록 도와줌
pandas → CSV 데이터를 불러와서 가공하는 데 필요
torch → PyTorch 기반 모델을 실행하는 데 필요
scikit-learn → 데이터 분할(train/test) 및 평가에 사용됨
