from smartcard.System import readers
from smartcard.util import toHexString

while True:
    card_readers = readers()

    if len(card_readers) < 1:
        print("No card readers found. Waiting for a reader to be connected...")
        continue

    reader = card_readers[0]
    connection = reader.createConnection()

    try:
        connection.connect()

        print("Waiting for a card to be inserted...")

        while True:
            # Send a command to read the MIFARE Classic 1k card's UID (Unique Identifier)
            # This is just an example; you may need to send other commands to read data.
            apdu_command = [0xFF, 0xCA, 0x00, 0x00, 0x00]
            response, sw1, sw2 = connection.transmit(apdu_command)

            if sw1 == 0x90 and sw2 == 0x00:
                uid = toHexString(response)
                print(f"MIFARE Classic 1k Card UID: {uid}")
                # You can add additional logic here to process the card data.

    except Exception as e:
        #print(f"Error: {e}")
        pass

    finally:
        connection.disconnect()
