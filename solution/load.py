from cmath import log
from sys import exc_info
import logging
logging.basicConfig(filename='./logs/shopping_patterns.log')
class Load:
    def load_data(self, spark, file_type=""):
        if file_type == "json":
            df = spark.read.option("recursiveFileLookup", "true").json("transactions")
        return df
    
    def to_landing(self, df):
        try:
            df.write.partitionBy("customer_id").mode("overwrite").json("output/")
            logging.info("Files saved to landing zone.")
        except Exception as err:
            logging.error(msg=str(err), exc_info=True)
            raise err
