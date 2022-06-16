from pyspark.sql import types as T
from pyspark.sql import functions as F

class Transform:
    def flatten(self, schema, prefix=None):
        fields = []
        for field in schema.fields:
            name = prefix + '.' + field.name if prefix else field.name
            dtype = field.dataType
            if isinstance(dtype, T.StructType):
                fields += self.flatten(dtype, prefix=name)
            else:
                fields.append(name)
        
        return fields


    def explodeDF(self, df):
        for (name, dtype) in df.dtypes:
            if "array" in dtype:
                df = df.withColumn(name, F.explode(name))

        return df

    def df_is_flat(self, df):
        for (_, dtype) in df.dtypes:
            if ("array" in dtype) or ("struct" in dtype):
                return False

        return True

    def flatJson(self, jdf):
        keepGoing = True
        while(keepGoing):
            fields = self.flatten(jdf.schema)
            new_fields = [item.replace(".", "_") for item in fields]
            jdf = jdf.select(fields).toDF(*new_fields)
            jdf = self.explodeDF(jdf)
            if self.df_is_flat(jdf):
                keepGoing = False

        return jdf