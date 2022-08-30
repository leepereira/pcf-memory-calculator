import pandas as pd
import argparse

# auth to cf
parser = argparse.ArgumentParser(description="Find the memory usage of a PCF foundation")
parser.add_argument('-f', '--filename', type=str, required=True, help="File name with PCF usage data")
args = parser.parse_args()
df = pd.read_csv(args.filename)

df.columns = df.columns.str.replace(' ', '')
df['OrgName'].replace({'system': 'PT-PaaS','credhub-service-broker-org': 'PT-PaaS','splunk-nozzle-org': 'PT-PaaS','p-dataflow': 'PT-PaaS', 'NewRelicServiceBroker-service-org': 'PT-PaaS'}, inplace=True)



totalMem = df['SpaceMemoryUsed'].sum()
ptMemUsage = df.groupby(["OrgName"]).agg({"SpaceMemoryUsed": "sum"}).sort_values(["SpaceMemoryUsed"],ascending=False).reset_index()
ptMemUsage['percentMemUsed'] = (ptMemUsage['SpaceMemoryUsed']/totalMem) * 100

ptMemUsage.to_csv("ptMem_usage.csv")

