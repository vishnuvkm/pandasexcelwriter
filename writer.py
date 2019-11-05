import pandas as pd

data = [
    {
        'k1': 1,
        'k2': 2
    },
    {
        'k1': '',
        'k2': 5
    }
]


def row_colour(row):
    if not row.k1:
        return ['background-color:' + 'red' for i in row]
    else:
        return ['background-color:' + 'white' for i in row]


writer = pd.ExcelWriter('out.xlsx', engine='xlsxwriter')

df1 = pd.DataFrame(data=data)
df1 = df1.style.apply(row_colour, axis=1)
df1.to_excel(writer, sheet_name='Sheet 1', index=False)

writer.save()
