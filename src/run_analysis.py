from db_connection import create_connection

def run_queries():
    connection = create_connection()
    cursor = connection.cursor()

    queries = {
        "total_sales_per_product": """
            SELECT PRODUCTID, SUM(FINALTOTAL) AS total_order_amount
            FROM ORDERDETAILS
            GROUP BY PRODUCTID
            ORDER BY total_order_amount DESC;
        """,

        "top_3_products": """
            SELECT PRODUCTID,
                   SUM(QUANTITY) AS total_quantity,
                   SUM(FINALTOTAL) AS total_volume
            FROM ORDERDETAILS
            GROUP BY PRODUCTID
            ORDER BY total_quantity DESC
            LIMIT 3;
        """,

        "premium_customers": """
            SELECT CUSTOMERID, SUM(TOTALPAID) AS total_order_value
            FROM ORDERS
            GROUP BY CUSTOMERID
            HAVING total_order_value > 1000;
        """,

        "product_sales_with_names": """
            SELECT P.PRODUCTID,
                   P.PRODUCTNAME,
                   SUM(OD.FINALTOTAL) AS total_order_amount
            FROM PRODUCTS P
            JOIN ORDERDETAILS OD ON P.PRODUCTID = OD.PRODUCTID
            GROUP BY P.PRODUCTID, P.PRODUCTNAME;
        """,

        "product_quantity_analysis": """
            SELECT P.PRODUCTID,
                   P.PRODUCTNAME,
                   COALESCE(SUM(OD.QUANTITY), 0) AS total_quantity_ordered
            FROM PRODUCTS P
            LEFT JOIN ORDERDETAILS OD ON P.PRODUCTID = OD.PRODUCTID
            GROUP BY P.PRODUCTID, P.PRODUCTNAME
            ORDER BY total_quantity_ordered DESC;
        """,

        "customers_same_city": """
            SELECT A.FIRSTNAME AS customer1,
                   B.FIRSTNAME AS customer2,
                   A.CITY
            FROM CUSTOMERS A
            JOIN CUSTOMERS B
              ON A.CUSTOMERID <> B.CUSTOMERID
             AND A.CITY = B.CITY;
        """
    }

    for name, query in queries.items():
        print(f"\n--- Running: {name} ---")
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            print(row)

    cursor.close()
    connection.close()

if __name__ == "__main__":
    run_queries()
