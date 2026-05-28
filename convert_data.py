import pandas as pd

# Load file
df = pd.read_excel("horizontal_crop_vertical_year_report.xlsx", header=[0,1,2])

# Flatten columns
df.columns = [
    '_'.join([str(i).strip() for i in col if str(i) != 'nan'])
    for col in df.columns
]

# Rename first columns
df = df.rename(columns={
    df.columns[0]: 'State',
    df.columns[1]: 'District',
    df.columns[2]: 'Year'
})

data = []

for _, row in df.iterrows():
    for col in df.columns:

        if "Area" in col and "Hectare" in col:
            try:
                parts = col.split('_')
                crop = parts[0]
                season = parts[1]

                # Clean numeric values
                def clean(val):
                    try:
                        return float(str(val).replace(",", "").strip())
                    except:
                        return None

                area = clean(row[col])

                prod_col = col.replace("Area (Hectare)", "Production (Tonnes)")
                yield_col = col.replace("Area (Hectare)", "Yield (Tonne/Hectare)")

                production = clean(row.get(prod_col, None))
                yield_val = clean(row.get(yield_col, None))

                # Only check area not null
                if area is not None:
                    data.append([
                        row['State'],
                        row['District'],
                        row['Year'],
                        crop,
                        season,
                        area,
                        production,
                        yield_val
                    ])

            except:
                continue

# Create DataFrame
new_df = pd.DataFrame(data, columns=[
    'State', 'District', 'Year',
    'Crop', 'Season', 'Area',
    'Production', 'Yield'
])

# Add extra features
new_df['Annual_Rainfall'] = 1000
new_df['Fertilizer'] = 50

# Drop nulls only if necessary
new_df = new_df.dropna(subset=['Area'])

# Save
new_df.to_csv("data/crop_data.csv", index=False)

print("✅ DONE! Rows created:", len(new_df))