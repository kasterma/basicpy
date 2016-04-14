import pandas as pd
import numpy as np
import yaml

# Read and normalize the data
config = yaml.load(open("bank-script-config.yaml"))

dat = pd.read_csv(config['inputfile'],
                  index_col=0,
                  parse_dates=True)
print(dat.head(20))

column_name_translations = {'Naam / Omschrijving': 'description',
                            'Rekening': 'account',
                            'Tegenrekening': 'otheracct',
                            'Code': 'code',
                            'Af Bij': 'afbij',
                            'Bedrag (EUR)': 'amount',
                            'MutatieSoort': 'type',
                            'Mededelingen': 'mededelingen'}
assert(all(colname in column_name_translations for colname in dat.columns))
dat.columns = [column_name_translations.get(colname, colname)
               for colname in dat.columns]

print(dat.dtypes)
dat.amount = dat.amount.map(lambda x: float(x.replace(',', '.')))
print(dat.dtypes)
dat = dat.assign(afbij=(dat.afbij == 'Af').map(lambda x: -1 if x else 1))
print(dat.dtypes)
dat = dat.assign(amount=dat.amount * dat.afbij)
print(dat.dtypes)

print(dat.head(20))


