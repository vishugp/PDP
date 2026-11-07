import pandas as pd
import numpy as np
loc = input("Enter database location: ")
if loc=='p':
  loc = '/content/sales_20-21.xlsx'
dataset = pd.ExcelFile(loc)

df = dataset.parse(dataset.sheet_names[3])
df.columns

def str_clean(name):
  rwords = ['LTD.','PVT.','PVT','LTD','LIMITED']
  s = str(name).upper()

  for i in rwords:
    if i in s:
      # print(s)
      s = s.replace(i,'')
  if 'SYSTEM' in s:
    s = s.replace('SYSTEM','SYSTEMS')
  if 'SYSTEMSS' in s:
    s = s.replace('SYSTEMSS','SYSTEMS')
    # print(s)
  s = s.strip()
  return s

companies = list()
counts = list()
indices = [8,3,5,6,9,1,7]
keys = list()
for i in indices:
  keys.append(df.columns[i])
print(keys)

pdp = np.empty([1000,100,len(keys)], dtype = "<U20")
print(pdp.shape)

for j in range(len(dataset.sheet_names)-1):
  df = dataset.parse(dataset.sheet_names[j])
  for i in range(df.shape[0]):
    # Column 2 is the Column of Organizations
    comp_name = str_clean(df[df.columns[2]][i])

    if comp_name == "NAN":
      continue
    if(comp_name not in companies):
      companies.append(comp_name)
      counts.append(1)
    
    else:
      counts[companies.index(comp_name)]+=1
      if(counts[companies.index(comp_name)] > 100):
        print(">100 : ",comp_name, counts[companies.index(comp_name)])
        print(j)


    index = companies.index(comp_name)
    # print(index,comp_name)
    for k in range(len(keys)):
      # print(df[keys[k]][i])
      pdp[index][counts[index]-1][k] = df[keys[k]][i]
      # print(pdp[index][counts[index]+1][k])




print("No. of Companies: ",len(companies))

print(counts)
companies.sort()
print(companies)
# for i in companies:
#   print(i)

for i in range(len(companies)):
  total = 0.0
  prods = list()
  count = list()  
  for j in range(counts[i]):

    total+= float(pdp[i][j][3])

    if (pdp[i][j][0] not in prods):
      prods.append(pdp[i][j][0])
      count.append(float(pdp[i][j][2]))
    else:
      count[prods.index(pdp[i][j][0])]+= float(pdp[i][j][2])
  # print(count)
  
  count_max = 0
  max_index = 0
  for z in range(len(count)):
    if count[z]>count_max:
      count_max = count[z]
      max_index = z

  
  # print(count,prods, "MAX = ",count_max," most common prod = ",prods[max_index])
  pdp[i][counts[i]+1][3] = total
  pdp[i][counts[i]+1][0] = prods[max_index]
  pdp[i][counts[i]+1][2] = count_max


  pdp[i][counts[i]+2][3] = total/counts[i]

# TOP SALE
def top_sale():
    max = 0.0
    ind = 0
    for i in range(len(companies)):
        amount = float(pdp[i][counts[i]+1][3])
        if amount > max:
            max = amount
            ind = i

    print("Best Company is : ",companies[ind]," which gives sales of Rs.",max)
    print("Most Common product type sold: ",pdp[i][counts[i]+1][0])

# TOP SALES (>threshold)
def top_sales():
    threshold = 10000000
    ind = list()
    for i in range(len(companies)):
        amount = float(pdp[i][counts[i]+1][3])
        if amount > threshold:
          ind.append(i)

    print(f"Companies with Sales > Rs.{threshold} : ")

    for i in ind:
        print(companies[i],f"\t Sale of Rs.{pdp[i][counts[i]+1][3]}\t",pdp[i][counts[i]+1][0],"\t",pdp[i][0][len(keys)-1])
        # print("Most Common product type sold: ",pdp[i][counts[i]+1][0])

###################################################################################################################################

# Company Name Wise Analysis

def name_analysis(i,zn):
  print("\nCompany No.",zn,"in the list is:")
  print("Name of the company: ",companies[i])
  print("No. of sale(s) : ",counts[i])
  print("Total Sales = ",pdp[i][counts[i]+1][3])

  indices = ''
  for j in range(len(keys)):
    indices+=keys[j]

    z = 25*(j+1) - len(indices)
    # print(z)
    for l in range (z):
      indices+= ' '
  
  indices = "  Sno  " + indices
  dash = ""
  for m in range(len(indices)):
    dash+="_"
  print(dash)
  print(indices)
  print(dash)
  
  for j in range(counts[i]):
    row = ''
    for k in range(pdp.shape[2]):
      row+=pdp[i][j][k]
      z = 25*(k+1) - len(row)
      # print(z)

      for l in range (z):
        row+= ' '
    
    spaces = ""
    for v in range(5 - len(str(j+1))):
      spaces +=" "
    row = "  " + str(j+1) + spaces + row
    print(row)

  print(dash)



while(True):
  n = input("\n\nEnter Company Name: ")
  n = n.upper()


  z=0
  for j in companies:
    if (n in j) and (j.index(n)==0 or j[j.index(n)-1]==" "):
      z+=1
      i = companies.index(j)
      name_analysis(i,z)
  if (z==0):
    print("Company with the word '",n,"' is not in the list!")


if __name__== '__main__':
    print("LOL")
