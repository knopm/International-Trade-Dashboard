import comtradeapicall

mydf = comtradeapicall.previewFinalData(typeCode='C', freqCode='M', clCode='HS', period='202205',
                                        reporterCode='36', cmdCode='91', flowCode='M', partnerCode=None,
                                        partner2Code=None,
                                        customsCode=None, motCode=None, maxRecords=500, format_output='JSON',
                                        aggregateBy=None, breakdownMode='classic', countOnly=None, includeDesc=True)

print(type(mydf)) 
print(mydf.head())       # show first 5 rows
print(mydf.info())       # get summary about columns, types, non-null counts
print(mydf.columns)      # list all columns names
print(mydf.describe())   # quick stats on numeric columns
