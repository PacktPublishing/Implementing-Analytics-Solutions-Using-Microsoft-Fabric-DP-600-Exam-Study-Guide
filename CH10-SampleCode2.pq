// Connecting to SQL Database in Power BI
// Use this script in Power BI's Power Query editor.

let 
    Source = Sql.Database("server_name", "database_name"),
    SalesData = Source{[Schema="dbo",Item="Sales"]}[Data]
in 
    SalesData




// Using Dataflows in Power BI to Merge Data Sources
// Use this script in Power BI's Power Query editor.

let 
    Source1 = Csv.Document(File.Contents("source1.csv")),
    Source2 = Sql.Database("server_name", "db_name")
in 
    Table.Combine({Source1, Source2})
