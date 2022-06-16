from ..solution.load import Load
from ..solution.extract import Extract
from ..solution.transform import Transform
import pytest
from pyspark.sql import SparkSession, DataFrame



@pytest.fixture(scope='session')
def spark():
    return SparkSession.builder \
      .master("local") \
      .appName("chispa") \
      .getOrCreate()

def test_extract():
    extract = Extract()
    customer_data = extract.extract_data(spark, file_type="csv", file_name="customers")
    assert type(customer_data) == DataFrame

    products_data = extract.extract_data(spark, file_type="csv", file_name="products")
    assert type(products_data) == DataFrame

def test_transform():
    transform = Transform()
    extract = Extract()

    data = transform.transform.flatJson(extract.extract_data(spark, file_type="json"))
    assert type(data) == DataFrame
