import pandas, sys

def read_pandas(fname: str) -> pandas.DataFrame:
    data = pandas.read_csv(fname, sep="|")
    return data

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python load_pandas.py <filename>")
        sys.exit(1)
    data = read_pandas(sys.argv[1])
    print(data.head(5))