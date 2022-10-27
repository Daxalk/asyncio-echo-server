import asyncio

async def connection(host, port):
    reader, writer = await asyncio.open_connection(host=host, port=port)
    return reader, writer

async def send_data(msg, writer):
    writer.write(msg.encode())
    await writer.drain()
    return 1

async def read_data(reader):
    data = await reader.read(1024)
    data.decode()
    return data

async def disconnection(writer):
    writer.close()
    return 1

async def main():
    try:
        host, port = '127.0.0.1', 9091
        msg = 'ABC123abc456'
        reader, writer = await connection(host, port)
        print(f'Соединение по адресу {host}' + ":" + f'{str(port)} произошло успешно!')

        await send_data(msg, writer)
        print(f'Сообщение {msg} успешно передано')

        data = await read_data(reader)
        if data:
            print(f"Сообщение {data} успешно получено")
        else:
            print('Сообщение не было получено')

        await disconnection(writer)
        print('Отключение от сервера')

    except ConnectionRefusedError:
        print('Соединение не установлено')

loop = asyncio.get_event_loop()
program = loop.create_task(main())
loop.run_until_complete(program)
