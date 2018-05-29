from xlrd import open_workbook
import urllib.request, os
from Inflation import Inflation
from Time import timestamp


def catchInflationFromIMF(InflationStruct):

    # Descarga temporalmente al archivo excel, copia los contenidos relevantes al table "values", y elimina el archivo
    direccion = "http://www.imf.org/external/datamapper//export/excel.php?indicator=PCPIPCH&geoitems=USA"
    urllib.request.urlretrieve(direccion, "US_inflation.xls")
    wb = open_workbook('US_inflation.xls')

    years = []
    rates = []

    for s in wb.sheets():
        col_names = s.row(0)
        for name, col in zip(col_names, range(s.ncols)):
            value = (s.cell(0, col).value)
            try:
                value = str(value)
            except:
                pass
            years.append(value)
        #print(years)


        col_names = s.row(0)
        for name, col in zip(col_names, range(s.ncols)):
            value = (s.cell(2, col).value)
            try:
                value = str(value)
            except:
                pass
            rates.append(value)
        #print(rates)

    os.remove("US_inflation.xls")

    rates_dict = {}

    #print(len(years))
    #print(len(rates))

    i = 1
    while (i < len(years)):
        rates_dict[years[i]] = rates[i]
        #print(str(years[i]) + ": " + str(rates[i]))
        i += 1

    #print(rates_dict)

    InflationStruct.inflation = rates_dict

    InflationStruct.timestamp = timestamp()

    return InflationStruct

