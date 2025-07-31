import sys
import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJECT_ROOT)

import pandas as pd
from jafgen import generate_customers, generate_orders, generate_payments

# Anzahl der zu generierenden Zeilen
n_customers = 100
n_orders = 500
n_payments = 800

# Generiere DataFrames
customers_df = generate_customers(n_customers)
orders_df = generate_orders(n_orders)
payments_df = generate_payments(n_payments)

print(customers_df.head())
print(orders_df.head())
print(payments_df.head())


