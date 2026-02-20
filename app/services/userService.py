async def get_all_users_service(conn):
    rows = await conn.fetch('SELECT * FROM "Users".users ORDER BY id ASC')
    print(rows)
    return [dict(row) for row in rows]
