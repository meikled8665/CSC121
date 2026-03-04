import csv


def getTotalSales():
    
    totalSales = []
    productID = []

    with open("sales.csv", "r", newline = "") as file:
        
        reader = csv.reader(file)
        next(reader, None)
        
        for row in reader:
            
            totalSales.append(float(row[4]) * float(row[5]))
            productID.append(row[2])

    return totalSales, productID


def saveTotalSales(totalSales, productID):
    
    fieldNames = ["Product ID", "Total Sales"]
    
    with open("total_sales.csv", "w", newline = "", ) as file:
        
        writer = csv.DictWriter(file, fieldnames = fieldNames)
        writer.writeheader()
        
        for i in range(len(totalSales)):
            writer.writerow({fieldNames[0] : productID[i], fieldNames[1] : str(f"${totalSales[i]:,.2f}")})
            

'''          
def totalSalesPerCust:
    pass
'''
            
saveTotalSales(getTotalSales()[0], getTotalSales()[1])