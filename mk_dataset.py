import pandas as pd
import os

input_folder = "/mnt/hdd1/moon/ev_data/sk"
output_file = "/mnt/hdd1/moon/ev_data/dataset/sk_data_label.csv"

def get_csv_files_by_folder(input_folder):
    file_paths = []
    for root, _, files in os.walk(input_folder):
        for file_name in files:
            if file_name.endswith('.csv'):
                file_paths.append(os.path.join(root, file_name))
    return file_paths



# CSV 파일 리스트
csv_files = get_csv_files_by_folder(input_folder)

# 데이터 리스트
data_list = []

# CSV 데이터를 텍스트로 변환
for file_path in csv_files:
    try:
        # 파일명 추출
        file_name = os.path.basename(file_path)

        # ✅ 이 파일이 어떤 종류인지 라벨(label) 설정
        
        #label = "sk-ev-origin"
        label = 0
        
        
        """
        if "sk" in file_name.lower():
            label = "sk-ev-origin"
        elif "betterwhy" in file_name.lower():
            label = "betterwhy-ev-origin"
        else:
            label = "unknown"
        """
        
        # CSV 파일 불러오기 (일부 행만 사용)
        df = pd.read_csv(file_path, nrows=10, dtype=str)  # 첫 10개 행만 사용

        text_representation = " | ".join(df.columns)  # 컬럼명 나열
        sample_data = df.iloc[0].fillna("").to_string()  # 첫 번째 행의 샘플 데이터
        csv_text = f"Columns: {text_representation} | Sample Data: {sample_data}"

        # 데이터 저장
        data_list.append({"text": csv_text, "label": label})

    except Exception as e:
        print(f"❌ {file_name} 처리 중 오류 발생: {e}")

# DataFrame으로 변환 후 저장
df_final = pd.DataFrame(data_list)
df_final.to_csv(output_file, index=False)

print(f"✅ 최종 데이터셋 저장 완료: {output_file}")