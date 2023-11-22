import pandas as pd

def concat_and_save(objs: list, filepath:str) -> bool:
    try:
        result = pd.concat(objs=objs, axis=0)
        result.to_csv(path_or_buf=filepath, encoding="utf-8", sep=";")
        return True
    except Exception as E:
        print("error:",E)
        return False

if __name__=="__main__":
    allStates = pd.read_csv(filepath_or_buffer="./data/BrazilAllStates_2012_2022/Incendio.csv", encoding="latin-1")
    amazon = pd.read_csv(filepath_or_buffer="./data/forestFireBrazilAmazon/amazon.csv", encoding="latin-1")

    concat_and_save(objs=[allStates, amazon], filepath="./data/timeSeriesBrazil.csv")
