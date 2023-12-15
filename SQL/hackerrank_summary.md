- take the remainder - MOD()
- remove duplicate - distinct

- Purpose: COUNT is used to count the number of rows that meet a specified condition.
  Example:
  sql
  Copy code
  SELECT COUNT(\*) AS NumberOfRows FROM TableName WHERE Condition;
  Result: It returns a single value, the count of rows.
  SUM:

- Purpose: SUM is used to calculate the sum of numerical values in a specific column.
  Example:
  sql
  Copy code
  SELECT SUM(NumericColumn) AS TotalSum FROM TableName WHERE Condition;
  Result: It returns a single value, the sum of the specified numeric column for the rows that meet the condition.

Round up - floor
Round down - ceil
    