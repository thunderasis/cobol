from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# 1. Iniciamos la sesión de Spark (El motor de Databricks)
spark = SparkSession.builder.appName("MigracionDataStage").getOrCreate()

# 2. Leemos los datos (Equivalente al "Source" en DataStage)
df_saldos = spark.read.table("raw_data.transacciones")

# 3. La lógica del Transformer: Calcular el Neto
# Aquí es donde la IA de Blitzy brilla traduciendo la regla de negocio
df_final = df_saldos.withColumn("Saldo_Neto", col("Ingreso") - col("Egreso"))

# 4. Guardamos en el Lakehouse (Equivalente al "Target")
df_final.write.format("delta").mode("overwrite").saveAsTable("gold_data.saldos_netos")

print("Proceso de ETL migrado exitosamente a Databricks.")