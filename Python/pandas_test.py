print("github")
import  pandas as pd
test=pd.read_excel("D:\MyCode\Python\877d23164be9238a23c24d37cfe44b80_f19a12e37c58223186bdf6e18a11b8da_8.xlsx",index_col=0,parse_dates=["时间"])
with pd.ExcelWriter("D:/MyCode/Python/test.xlsx") as writer:
    test.to_excel(writer,sheet_name="total")
    labels=test.厂商.unique()
    for label in labels:
        test1=test[test["厂商"]==label]
        test1.to_excel(writer, sheet_name=label)
    writer.save()


