import pandas as pd
import gspread as gs

# <id>@eyantra-377711.iam.gserviceaccount.com email add
credfile = "eyantra-377711-e0703838152b.json"
gc = gs.service_account(credfile)
sheet = gc.open('eYantra')
wk = sheet.worksheet('testsheet')
db = wk.get_all_records()
db = pd.DataFrame(db)
print(db)
