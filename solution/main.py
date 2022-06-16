import imp
from pyspark.sql import SparkSession
import logging
from sys import exc_info
from load import Load
from extract import Extract
from transform import Transform

logging.basicConfig(filename='./logs/shopping_patterns.log')


class ShoppingPatternApp:
    def __init__(self, params) -> None:
        try:
            self.extract = Extract()
            self.transform = Transform()
            self.load = Load()

        except Exception as err:
            logging.error(msg=str(err), exc_info=True)
            raise err
    
    def run(self, spark:SparkSession):
        try:
            shoping = self.transform.flatJson(self.extract.extract_data(spark, file_type="json"))
            customers_df = self.extract.extract_data(spark, file_type="csv", file_name="customers")
            products_df = self.extract.extract_data(spark, file_type="csv", file_name="products")
            customers_df.createOrReplaceTempView("customers")
            products_df.createOrReplaceTempView("products")
            shoping.createOrReplaceTempView("shoping")
            ans = spark.sql(
                """WITH cte AS (
                    SELECT s.customer_id AS customer_id, c.loyalty_score AS loyalty_score, p.product_id AS product_id, p.product_category AS product_category 
                    FROM shoping s 
                        INNER JOIN customers c 
                        ON s.customer_id = c.customer_id 
                            INNER JOIN products p 
                            ON s.basket_product_id=p.product_id
                ), 
                sum_cte AS (
                    SELECT 
                    customer_id, COUNT(product_id) AS purchase_count 
                    FROM cte 
                    GROUP BY customer_id
                ) 
                SELECT 
                c.customer_id AS customer_id, loyalty_score, product_id, product_category, purchase_count 
                FROM cte c 
                INNER JOIN  sum_cte sc 
                    ON c.customer_id=sc.customer_id 
                ORDER BY customer_id;"""
            )
            self.load.to_landing(df=ans)
        except Exception as err:
            logging.error(msg=str(err), exc_info=True)
            raise err