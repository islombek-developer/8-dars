# import psycopg2 
# import csv

# data = {
#     "host": "localhost",
#     "port": 5432,
#     "database": "education",
#     "user": "postgres",
#     "password": "postgres"
# }

# try:
#     connection = psycopg2.connect(**data)
#     cursor = connection.cursor()
#     cursor.execute("SELECT * FROM people_data WHERE age > 16 ORDER BY age;")
#     people_data = cursor.fetchall()
#     file_name = "people_data.csv"

#     with open(file_name, "w", newline='',encoding='utf-8') as csv_file:
#         writer = csv.writer(csv_file)
        
#         for i in people_data:
#             writer.writerow(i)


# except psycopg2.Error as e:
#     print(f"Error: {e}")
# finally:
#     if connection:
#         cursor.close()
#         connection.close()
#         print("postgres yopildi")
