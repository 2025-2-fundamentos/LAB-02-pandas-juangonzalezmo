import pandas as pd

RUTA_TBL0 = "files/input/tbl0.tsv"
RUTA_TBL1 = "files/input/tbl1.tsv"
RUTA_TBL2 = "files/input/tbl2.tsv"


def cargar_tbl0():
    return pd.read_csv(RUTA_TBL0, sep="\t")


def cargar_tbl1():
    return pd.read_csv(RUTA_TBL1, sep="\t")


def cargar_tbl2():
    return pd.read_csv(RUTA_TBL2, sep="\t")