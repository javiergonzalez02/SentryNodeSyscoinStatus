import requests
import json
import time

# RPC connection configuration
rpc_user = 'yourusername'
rpc_password = 'yourpassword'
rpc_port = '8336'
rpc_url = f'http://{rpc_user}:{rpc_password}@127.0.0.1:{rpc_port}'


# Function to make RPC calls to the wallet
def call_rpc(method, params=[]):
    headers = {'content-type': 'application/json'}
    payload = json.dumps({
        "method": method,
        "params": params,
        "jsonrpc": "2.0",
        "id": 0,
    })

    try:
        response = requests.post(rpc_url, headers=headers, data=payload)
        if response.status_code == 200:
            return response.json()
        else:
            print(f'Error in RPC request: {response.status_code}')
            print(response.text)
            return None
    except requests.exceptions.RequestException as e:
        print(f'Exception during RPC request: {e}')
        return None


# Function to get the masternode list and filter by collateral address
def get_masternode_by_collateral(collateral_address):
    response = call_rpc('masternode_list')
    if response:
        masternodes = response.get('result', {})
        for mn in masternodes.values():
            if mn.get('collateraladdress') == collateral_address:
                return mn
    return None


# Main function
if __name__ == '__main__':
    collateral_address = input('Please enter the collateral address: ')

    while True:
        masternode = get_masternode_by_collateral(collateral_address)

        if masternode:
            print(json.dumps(masternode, indent=4))
        else:
            print(f'No masternode found with the collateral address: {collateral_address}')

        # Wait 30 minutes (1800 seconds) before making another request
        print('Waiting 30 minutes for the next query...')
        time.sleep(1800)
