import asyncio

async def handle_echo(reader, writer):
    print('Сервер запущен!')
    data = await read_data(reader)
    if data:
        print(f"Сообщение {data} успешно получено")
    else:
        print('Сообщение не было получено')

    await send_data(data, writer)
    print(f'Сообщение {data} успешно передано')
    writer.close()
    

async def send_data(msg, writer):
    writer.write(msg)
    await writer.drain()
    return 1

async def read_data(reader):
    data = await reader.read(1024)
    data.decode()
    return data

async def server_close(server):
    server.close()
    return 1

async def main():
    host, port = '127.0.0.1', 9091
    server = await asyncio.start_server(client_connected_cb=handle_echo, host=host, port=port)
    async with server:
        await server.serve_forever()

asyncio.run(main())
