import pyodbc

def show_odbc_sources():
    sources = pyodbc.dataSources()
    dsns = sources.keys()
    sl = []
    for dsn in dsns:
        sl.append('%s [%s]' % (dsn, sources[dsn]));
        print(dsn);

show_odbc_sources()

cnxn = pyodbc.connect(DSN="ODBC 18")

print(cnxn)
cursor = cnxn.cursor()
cursor.execute("select * from Zendesk.dbo.LOAD_TICKET_FIELDS")
row = cursor.fetchall()

print(row)
