import pandas as pd
import os

# ── FUNCIÓN 1: Cargar el archivo ──
def cargar_archivo(ruta):
    if not os.path.exists(ruta):
        raise FileNotFoundError("El archivo no existe")
    try:
        df = pd.read_csv(ruta)
    except Exception:
        raise ValueError("Error al leer el archivo CSV")
    return df

# ── FUNCIÓN 2: Validar los datos ──
def validar_datos(df):
    columnas_esperadas = {"fecha", "descripcion", "monto"}
    if not columnas_esperadas.issubset(df.columns):
        raise ValueError("El archivo no tiene el formato correcto")
    if df["monto"].isnull().any():
        raise ValueError("Hay valores nulos en los montos")

# ── FUNCIÓN 3: Calcular el balance ──
def calcular_balance(df):
    return df["monto"].sum()

# ── FUNCIÓN 4: Detectar transacciones sospechosas ──
def detectar_sospechosas(df, limite=1000000):
    sospechosas = df[df["monto"] > limite]
    return sospechosas

# ── FUNCIÓN 5: Exportar a CSV ──
def exportar_sospechosas(sospechosas):
    if sospechosas.empty:
        print("No hay transacciones sospechosas.")
    else:
        sospechosas.to_csv("sospechosas.csv", index=False)
        print(f"Se encontraron {len(sospechosas)} transacción(es) sospechosa(s).")
        print("Exportadas a: sospechosas.csv")

# ── FUNCIÓN PRINCIPAL ──
def main():
    archivo = input("Ingrese nombre del archivo: ").strip()
    try:
        df = cargar_archivo(archivo)
        
        validar_datos(df)
        total = calcular_balance(df)
        print(f"Balance total: {total}")
        sospechosas = detectar_sospechosas(df)
        print(f"Sospechosas encontradas: {len(sospechosas)}")    
        exportar_sospechosas(sospechosas)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()