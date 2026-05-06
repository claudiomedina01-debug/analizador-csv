import pandas as pd
import os


def cargar_archivo(ruta):
	if not ruta:
		raise ValueError("Debe ingresar el nombre del archivo")

	if not os.path.exists(ruta):
		raise FileNotFoundError("El archivo no existe")

	try:
		df = pd.read_csv(ruta)
	except pd.errors.EmptyDataError as exc:
		raise ValueError("El archivo CSV esta vacio") from exc
	except pd.errors.ParserError as exc:
		raise ValueError("Error de formato al leer el archivo CSV") from exc
	except Exception as exc:
		raise ValueError("Error inesperado al leer el archivo CSV") from exc

	return df


def validar_datos(df):
	if df.empty:
		raise ValueError("El archivo CSV no contiene registros")

	columnas_esperadas = {"fecha", "descripcion", "monto"}
	if not columnas_esperadas.issubset(df.columns):
		raise ValueError("El archivo no tiene el formato correcto")

	montos = pd.to_numeric(df["monto"], errors="coerce")
	if montos.isnull().any():
		raise ValueError("Hay valores nulos o no numericos en los montos")


def calcular_balance(df):
	montos = pd.to_numeric(df["monto"], errors="coerce")
	return montos.sum()


def main():
	archivo = input("Ingrese nombre del archivo: ").strip()

	try:
		df = cargar_archivo(archivo)
		validar_datos(df)
		total = calcular_balance(df)
		print(f"Balance total: {total}")
	except (FileNotFoundError, ValueError) as e:
		print(f"Error: {e}")


if __name__ == "__main__":
	main()