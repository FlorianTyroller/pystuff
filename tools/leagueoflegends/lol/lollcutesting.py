from lcu_driver import Connector
import time

connector = Connector()

@connector.ws.register('/lol-gameflow/v1/gameflow-phase', event_types=('UPDATE',))
async def gameflow_update(connection, event):
    print(f"[INFO] Gameflow Phase Updated: {event.data}")

@connector.ws.register('/lol-champ-select/v1/session', event_types=('CREATE', 'UPDATE'))
async def champ_select_update(connection, event):
    print(f"[INFO] Champ Select Update: {event.data}")

@connector.ready
async def connect(connection):
    print('[INFO] LCU API connected')

@connector.close
async def disconnect(_):
    print('[INFO] The client has been closed')


if __name__ == "__main__":
    connector.start()
    while True:
        try:
            time.sleep(1)  # Sleep to not overload with output
        except KeyboardInterrupt:
            connector.stop()  # Allow for clean exit
            print("[INFO] Script stopped")
            break