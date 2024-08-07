# Syscoin Configuration and Script Setup

To get started with running the script, follow these steps to configure your `syscoin.conf` file:

## 1. Update `syscoin.conf`

Add the following lines to your `syscoin.conf` file:

server=1
rpcuser=yourusername
rpcpassword=yourpassword
rpcallowip=127.0.0.1
rpcport=8336

## Configuration Details

- **`server=1`**: Enables the RPC server.
- **`rpcuser=yourusername`**: Sets the RPC username. Replace `yourusername` with your chosen username.
- **`rpcpassword=yourpassword`**: Sets the RPC password. Replace `yourpassword` with your chosen password.
- **`rpcallowip=127.0.0.1`**: Allows connections only from localhost.
- **`rpcport=8336`**: Specifies the RPC server port (default: 8336).

## 2. Restart the Wallet

After updating the `syscoin.conf` file, you need to restart your Syscoin wallet for the changes to take effect.

## 3. Run the Script

Once the wallet is restarted, you can run the script as intended.

**Note:** The placeholders `yourusername` and `yourpassword` can be replaced with any credentials in the `syscoin.conf` file, just make sure the ones in the script match the ones in the syscoin.config file.

For further assistance, refer to the [Syscoin documentation](https://docs.syscoin.org) and [Syscoin Core](https://syscoincore.org).