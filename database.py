import aiomysql
from customer import Customer

DB_CONFIG = {
    "host": "localhost",
    "port": 3307,  # Default MySQL/MariaDB port
    "user": "root",
    "password": "123456",
    "db": "DemoDB",
}

async def get_db():
    pool = await aiomysql.create_pool(**DB_CONFIG)
    async with pool.acquire() as conn:
        async with conn.cursor(aiomysql.DictCursor) as cur:
            yield cur
    pool.close()
    await pool.wait_closed()

async def create(c: dict):
    query = "INSERT INTO Customer (CustomerId, Name) VALUES (%s, %s)"
    async for cur in get_db():
        await cur.execute(query, (c["CustomerId"], c["Name"]))
        await cur.connection.commit()
    return c

async def read_one(id: str):
    query = "SELECT * FROM Customer WHERE CustomerId = %s"
    async for cur in get_db():
        await cur.execute(query, (id,))
        result = await cur.fetchone()
        if result:
            return Customer(**result)
    return None

async def read_all():
    query = "SELECT * FROM Customer"
    customers = []
    async for cur in get_db():
        await cur.execute(query)
        results = await cur.fetchall()
        customers = [Customer(**row) for row in results]
    return customers

async def update(id: str, name: str):
    query = "UPDATE Customer SET Name = %s WHERE CustomerId = %s"
    async for cur in get_db():
        await cur.execute(query, (name, id))
        await cur.connection.commit()
    return await read_one(id)

async def delete(id: str):
    query = "DELETE FROM Customer WHERE CustomerId = %s"
    async for cur in get_db():
        await cur.execute(query, (id,))
        await cur.connection.commit()
        return cur.rowcount > 0  # Return True if deleted
