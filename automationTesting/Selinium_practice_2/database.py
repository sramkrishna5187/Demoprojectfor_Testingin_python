import os
import cx_oracle

os.environ('path')='E://newfile'

con=cx_oracle.connect('hr','hr',"localhost:1521/pbdoracl")
cur=con.cursor()

query =select * from selectemployee

cur.execute(query)

for col in cur:
    print(col[0]," ",col[1])

print("the Task is completed")

cur.close
con.close






