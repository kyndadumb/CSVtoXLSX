import os
import pandas as pd

if __name__ == "__main__":
    current_path = os.path.dirname(os.path.abspath(__file__))
    csv_files = [file for file in os.listdir(current_path) if file.endswith('.csv')]

    if len(csv_files) == 0:
        print("Keine CSV-Datei gefunden!")
        exit()

    csv_file = os.path.join(current_path, csv_files[0])
    df = pd.read_csv(csv_file, delimiter=';')

    selected_columns = ['Column1', 'Column2']
    df_selected = df[selected_columns]

    xlsx = os.path.join(current_path, "result.xlsx")
    df_selected.to_excel(xlsx, index=False)

    print(f"{xlsx} erstellt!")