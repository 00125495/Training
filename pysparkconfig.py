
spark = SparkSession.builder \
    .master("local") \
    .appName("test") \
    .config("spark.some.config.option", "somevalue")
    .enableHiveSupport()
    .getOrCreate()

config(key=None, value=None, conf=None)

config(conf=SparkConf())

config("k", "v")

spark.conf.get("k")