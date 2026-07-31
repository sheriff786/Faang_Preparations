# Target Table Identification Using ML (Supervised Classification)

## Problem Statement
Given a database with multiple tables, automatically identify which table is the **target table** (relevant for our use case) using a trained ML model — **Yes (take it)** or **No (skip it, move to next)**.

---

## Strategy Overview

```
[Collect Table Metadata] → [Create Labeled CSV] → [Feature Engineering] → [Train XGBoost/LightGBM] → [Deploy for Real-Time Prediction]
```

---

## Step 1: Extract Table Header/Metadata Features

For every table in the database, extract these features and store in a CSV:

| Feature | Description |
|---------|-------------|
| `table_name` | Name of the table |
| `num_columns` | Total number of columns |
| `num_rows` | Total row count |
| `has_id_column` | 1 if table has an ID/primary key column, else 0 |
| `has_date_column` | 1 if any column has date/timestamp type |
| `has_numeric_columns` | Count of numeric columns |
| `has_text_columns` | Count of text/varchar columns |
| `has_foreign_key` | 1 if table has foreign key references |
| `avg_null_percentage` | Average null % across all columns |
| `column_name_keywords` | Encoded presence of domain keywords in column names |
| `table_name_keyword_match` | 1 if table name contains domain-relevant keywords |
| `num_unique_values_ratio` | Avg(unique values / total rows) across columns |
| `table_size_mb` | Size of table in MB |

---

## Step 2: Sample Training Data (CSV)

```csv
table_name,num_columns,num_rows,has_id_column,has_date_column,has_numeric_columns,has_text_columns,has_foreign_key,avg_null_percentage,table_name_keyword_match,num_unique_values_ratio,table_size_mb,is_target
customer_transactions,12,500000,1,1,8,4,1,2.5,1,0.65,120.5,1
user_logs,5,2000000,1,1,2,3,0,15.0,0,0.12,450.0,0
product_catalog,8,15000,1,0,4,4,0,1.2,0,0.85,5.2,0
order_details,15,750000,1,1,10,5,1,3.1,1,0.55,200.3,1
system_audit,4,10000000,1,1,1,3,0,0.5,0,0.02,800.0,0
payment_history,10,600000,1,1,7,3,1,1.8,1,0.60,150.0,1
temp_staging,20,100,0,0,10,10,0,45.0,0,0.95,0.1,0
sales_summary,9,300000,1,1,6,3,1,2.0,1,0.50,80.0,1
error_logs,3,5000000,1,1,1,2,0,0.1,0,0.01,600.0,0
inventory_master,11,50000,1,0,7,4,1,5.0,0,0.70,15.0,0
revenue_monthly,7,400000,1,1,5,2,1,1.5,1,0.45,90.0,1
config_settings,6,200,0,0,2,4,0,0.0,0,0.99,0.01,0
shipment_tracking,13,650000,1,1,9,4,1,2.8,1,0.58,180.0,1
db_migrations,4,500,1,1,1,3,0,0.0,0,0.90,0.05,0
customer_feedback,8,200000,1,1,3,5,0,10.0,0,0.40,40.0,0
```

---

## Step 3: Feature Engineering

```python
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load data
df = pd.read_csv("table_metadata.csv")

# Features (drop table_name - it's just identifier, drop target)
feature_cols = [
    'num_columns', 'num_rows', 'has_id_column', 'has_date_column',
    'has_numeric_columns', 'has_text_columns', 'has_foreign_key',
    'avg_null_percentage', 'table_name_keyword_match',
    'num_unique_values_ratio', 'table_size_mb'
]

X = df[feature_cols]
y = df['is_target']  # 1 = Yes (take it), 0 = No (skip it)
```

---

## Step 4: Train Model (XGBoost + LightGBM)

### XGBoost Approach

```python
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import classification_report

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# XGBoost
xgb_model = XGBClassifier(
    n_estimators=100,
    max_depth=4,
    learning_rate=0.1,
    use_label_encoder=False,
    eval_metric='logloss'
)

xgb_model.fit(X_train, y_train)
y_pred = xgb_model.predict(X_test)

print(classification_report(y_test, y_pred))
```

### LightGBM Approach

```python
import lightgbm as lgb

lgb_model = lgb.LGBMClassifier(
    n_estimators=100,
    max_depth=4,
    learning_rate=0.1,
    num_leaves=31
)

lgb_model.fit(X_train, y_train)
y_pred_lgb = lgb_model.predict(X_test)

print(classification_report(y_test, y_pred_lgb))
```

---

## Step 5: Real-Time Prediction Pipeline

```python
import joblib

# Save trained model
joblib.dump(xgb_model, "target_table_classifier.pkl")

# --- REAL SCENARIO USAGE ---
def identify_target_table(database_connection):
    """
    Iterate through all tables in DB.
    For each table: extract metadata → predict → take or skip.
    """
    model = joblib.load("target_table_classifier.pkl")
    target_tables = []

    all_tables = get_all_tables(database_connection)  # Your DB utility

    for table in all_tables:
        # Extract features for this table
        features = extract_table_metadata(database_connection, table)
        
        # Predict
        prediction = model.predict([features])[0]
        confidence = model.predict_proba([features])[0][1]

        if prediction == 1:
            print(f"✓ YES - Take table: {table} (confidence: {confidence:.2f})")
            target_tables.append(table)
        else:
            print(f"✗ NO  - Skip table: {table} (confidence: {1-confidence:.2f})")
            # Move to next table

    return target_tables
```

---

## Step 6: Metadata Extraction Utility

```python
import sqlalchemy
from sqlalchemy import inspect

def extract_table_metadata(engine, table_name):
    """Extract features from a single table for prediction."""
    inspector = inspect(engine)
    columns = inspector.get_columns(table_name)
    pk = inspector.get_pk_constraint(table_name)
    fks = inspector.get_foreign_keys(table_name)

    # Domain keywords (customize per use case)
    DOMAIN_KEYWORDS = ['transaction', 'order', 'payment', 'sale', 'revenue', 'shipment']

    num_columns = len(columns)
    has_id = 1 if pk.get('constrained_columns') else 0
    has_date = 1 if any(str(c['type']).lower() in ['date', 'datetime', 'timestamp'] for c in columns) else 0
    has_numeric = sum(1 for c in columns if 'int' in str(c['type']).lower() or 'float' in str(c['type']).lower())
    has_text = sum(1 for c in columns if 'varchar' in str(c['type']).lower() or 'text' in str(c['type']).lower())
    has_fk = 1 if fks else 0
    keyword_match = 1 if any(kw in table_name.lower() for kw in DOMAIN_KEYWORDS) else 0

    # Get row count and null stats (sample for large tables)
    with engine.connect() as conn:
        row_count = conn.execute(f"SELECT COUNT(*) FROM {table_name}").scalar()
        # Calculate avg null percentage (simplified)
        null_pcts = []
        for col in columns:
            null_count = conn.execute(
                f"SELECT COUNT(*) FROM {table_name} WHERE {col['name']} IS NULL"
            ).scalar()
            null_pcts.append((null_count / max(row_count, 1)) * 100)

    avg_null = sum(null_pcts) / max(len(null_pcts), 1)

    return [
        num_columns, row_count, has_id, has_date,
        has_numeric, has_text, has_fk, avg_null,
        keyword_match, 0.5, 50.0  # unique_ratio and size estimated
    ]
```

---

## Decision Flow (Production)

```
┌─────────────────────┐
│  Connect to DB      │
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│  Get All Tables     │
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│  For Each Table:    │
│  Extract Metadata   │
└──────────┬──────────┘
           ▼
┌─────────────────────┐
│  Model Predicts     │
│  (XGBoost/LightGBM) │
└──────────┬──────────┘
           ▼
    ┌──────┴──────┐
    │             │
    ▼             ▼
┌────────┐  ┌────────────┐
│ YES=1  │  │   NO=0     │
│ TAKE IT│  │ SKIP/LEAVE │
└────────┘  └────────────┘
```

---

## Key Points

| Aspect | Detail |
|--------|--------|
| **Model Type** | Binary Classification (Yes/No) |
| **Algorithms** | XGBoost, LightGBM (gradient boosting) |
| **Input** | Table metadata/header features |
| **Output** | 1 = Target Table (Take), 0 = Not Target (Skip) |
| **Training Data** | Manually labeled CSV of table metadata |
| **Threshold** | Default 0.5, tune based on precision/recall needs |

---

## How to Build Training Data (One-Time Effort)

1. Connect to your databases
2. Run metadata extraction on ALL tables
3. Manually label each row: `is_target = 1` or `is_target = 0`
4. Save as CSV → Train model → Deploy

Once trained, the model handles new/unseen databases automatically.
