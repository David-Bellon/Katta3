import pandas as pd

def clean_data(df):
    to_drop = []
    for e in df.columns:
        if e in ("model", "manufacturer", "cost_in_credits", "max_atmosphering_speed", "cargo_capacity", "consumables", "vehicle_class", "hyperdrive_rating", "MGLT", "starship_class"):
            to_drop.append(e)
    df = df.drop(columns=to_drop)
    df.columns = ["nombre", "largo", "tripulacion", "pasajeros"]
    df = df.dropna()
    df = df.reset_index().drop(columns=["index"])
    return df

df1 = pd.read_csv(r"exaclau\Ejer3\vehicles.csv")
df2 = pd.read_csv(r"exaclau\Ejer3\starships.csv")
df1 = clean_data(df1)
df2 = clean_data(df2)

df = pd.concat([df1, df2], ignore_index=True)
df = df.reset_index().drop(columns=["index"])
df.to_csv(r"exaclau\Ejer3\data.csv")