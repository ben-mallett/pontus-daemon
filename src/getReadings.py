import random
import psycopg2
import os

def getTemp() -> float:
    """
    Returns a random reasonable temperature value
    """
    return round(random.uniform(70.0, 79.9), 2)

def getPH() -> float:
    """
    Returns a random reasonable pH value
    """
    return round(random.uniform(7.8, 8.4), 2)

def getAlkalinity() -> float:
    """
    Returns a random reasonabl alkalinity value
    """
    return round(random.uniform(7.0, 12.0), 2)

def getConductivity() -> float:
    """
    Returns a random reasonable conductivity value
    """
    return round(random.uniform(50.0, 55.0), 2)

def getNitrates() -> float:
    """
    Returns a random reasonable nitrate value
    """
    return round(random.uniform(0.0, 5.0), 2)

def getNitrites() -> float:
    """
    Returns a random reasonable nitrite value
    """
    return round(random.uniform(0.0, 0.1), 2)

def getAmmonia() -> float:
    """
    Returns a random reasonable ammonia value
    """
    return round(random.uniform(0.0, 0.25), 2)

def connectToDB():
    """
    Establishes a connection to the CloudSQL PostgreSQL database.
    """
    connection = psycopg2.connect(
        dbname="pontus",
        user="postgres",
        password="Chalkdust91-",
        host="34.23.109.253",  
        port="5432"
    )
    return connection

def uploadSensorReading(connection, data_type: str, value: float, device_id: int):
    """
    Uploads a sensor reading to the SensorReading table.
    """
    cursor = connection.cursor()
    cursor.execute(
        """
        INSERT INTO "SensorReading" (dataType, value, deviceId)
        VALUES (%s, %s, %s)
        """,
        (data_type, value, device_id)
    )
    connection.commit()
    cursor.close()

if __name__ == '__main__':
    connection = connectToDB()

    deviceId = os.getenv('DATABASE_DEVICE_ID')

    readings = {
        'TEMPERATURE': getTemp(),
        'PH': getPH(),
        'ALKALINITY': getAlkalinity(),
        'AMMONIA': getAmmonia(),
        'CONDUCTIVITY': getConductivity(),
        'NITRITES': getNitrites(),
        'NITRATES': getNitrates()
    }
    print(readings)
    for dataType, value in readings.items():
        print('uploading ')
        uploadSensorReading(connection, dataType, value, deviceId)

    connection.close()