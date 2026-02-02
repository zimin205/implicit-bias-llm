from datasets import load_dataset
import json

DATASET_NAME = "heegyu/bbq"   # 필요하면 나중에 바꿀 수 있음

def main():
    ds = load_dataset(DATASET_NAME, trust_remote_code=True)
    print("=== Dataset loaded ===")
    print("Dataset name:", DATASET_NAME)
    print("Splits:", list(ds.keys()))
    
    # 우선 첫 번째 split 기준으로 구조 확인
    split = "test" if "test" in ds else list(ds.keys())[0]
    data = ds[split]

    print("\n=== Split info ===")
    print("Using split:", split)
    print("Num rows:", len(data))

    # 필드(컬럼) 이름 확인
    print("\n=== Column names ===")
    print(data.column_names)

    # 첫 샘플 1개 출력 (너무 길면 일부만)
    ex0 = data[0]
    print("\n=== Example[0] keys ===")
    print(list(ex0.keys()))

    # 보기 좋게 JSON 형태로 일부만 프린트
    # (context가 너무 길면 잘라서 보여줌)
    pretty = {}
    for k, v in ex0.items():
        if isinstance(v, str) and len(v) > 400:
            pretty[k] = v[:400] + "...(truncated)"
        else:
            pretty[k] = v
    print("\n=== Example[0] preview ===")
    print(json.dumps(pretty, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
