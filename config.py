import sys

DATABASE_PATH = "clientes.csv"

if "pytest" in sys.modules:
    DATABASE_PATH = "test_clientes.csv"