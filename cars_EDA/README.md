# 🚗 Cars Dataset EDA Dashboard

This project is an **interactive Streamlit dashboard** for exploring and analyzing a Cars dataset.  
It helps visualize car prices, fuel types, seating capacity, body types, and more in a **simple and user-friendly way**.

---

## 📂 Features

- 📋 Raw dataset preview  
- 📊 Dataset statistics summary  
- 💰 Average starting price by fuel type  
- 🚙 Car count by body type  
- 🪑 Seating capacity distribution  
- 📈 Correlation heatmap of numerical features  
- 📏 Price range histogram (Ending Price – Starting Price)  

---

## ⚙️ Installation & Usage

1. Clone this repository or download the files.  

```bash
git clone https://github.com/jhaamit07/cars_EDA.git
cd cars_EDA
```

2.Create a virtual environment (optional but recommended).

```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```

3. Install dependencies
   
```bash
pip install -r requirements.txt
```

4. Run the Streamlit App
   
```bash
streamlit run cars_app.py
```
