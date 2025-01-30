# Jobsity Data Engineering Challenge Solution

## Author
**Mario Lara**

---

## 🚀 Set Up
### **Prerequisites**
Ensure you have **Python 13.1** installed and the following libraries:
- `pandas`
- `psycopg2`
- `tqdm`

### **PostgreSQL Requirements**
- A running **PostgreSQL instance** with the **PostGIS extension** enabled.
- To enable PostGIS, execute the following SQL command:
  ```sql
  CREATE EXTENSION postgis;
  ```

---

## ⚙️ Configuration
1. **Database Connection**:
   - Edit the file **`pg_connector.py`**.
   - Update the **`DB_CONFIG`** dictionary with the correct credentials for your PostgreSQL instance.

2. **Source Data Directory**:
   - Create a folder named **`source_data`** in the same directory as the scripts.
   - Place your CSV files in this folder using the same format as the sample data.

---

## 📂 File Descriptions
### **SQL Files**
| File Name | Description |
|-----------|------------|
| `pg_init.sql` | Removes and regenerates the database schema. |
| `pg_transform_trips.sql` | Transforms raw data to match the database schema. |
| `weekly_avg_region.sql` | Retrieves the weekly average of trips for a **specific region** (filtered by region name). |
| `weekly_avg_bound_box.sql` | Retrieves the weekly average of trips for a **specific bounding box** (filtered using four coordinates). |
| `latest_ds.sql` | **Bonus query**: Finds the latest data source appearing in the two most frequently occurring regions. |
| `cheap_mobile.sql` | **Bonus query**: Displays regions where the data source **"cheap_mobile"** appears. |

### **Python Scripts**
| File Name | Description |
|-----------|------------|
| `pg_connector.py` | Handles PostgreSQL connections, allowing configuration in one place. |
| `pg_trip_ingestor.py` | **Ingests data** from the `source_data` folder or **resets the database schema** based on the provided argument. |
| `test_data_generator.py` | Generates **test trip data** in the same format as the sample. |
| `weekly_avg_by_region.py` | Executes the **weekly trip average query for a region** (region name is provided as an argument). |
| `weekly_avg_by_bound_box.py` | Executes the **weekly trip average query for a bounding box** (coordinates provided as arguments). |
| `bonus.py` | Executes **bonus queries** based on the provided argument. |

### **Other**
| File Name | Description |
|-----------|------------|
| `aws_sketch.drawio` | A diagram of an alternative implementation for this challenge, had I done it purely in AWS. |
---

## 📌 Notes
- Ensure all dependencies are installed before running any scripts.
- Use **Python 13.1** (or the latest compatible version).
- Check `pg_connector.py` for correct database credentials.

