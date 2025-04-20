"""
readme: 所有api接口的实现依赖于https://github.com/cornucopiaa/btcscan-org/blob/master/API.md
"""
import requests
import json
# 最新区块hash
def get_latest_block_hash():
    try:
        response = requests.get('https://btcscan.org/api/blocks/tip/hash')
        if response.status_code == 200:
            return response.text
        else:
            print('\033[31m' + response.text + '\033[0m')
            return None
    except Exception as e:
        print(e)
        return None

# 总区块高度
def get_blocks_height():
    try:
        response = requests.get('https://btcscan.org/api/blocks/tip/height')
        if response.status_code == 200:
            return response.text
        else:
            print('\033[31m' + response.text + '\033[0m')
            return None
    except Exception as e:
        print(e)
        return None
# 获取某一区块信息(不包含交易信息transactions)
def get_single_block_info(hash):
    try:
        response = requests.get(f'https://btcscan.org/api/block/{hash}')
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            print('\033[31m' + response.text + '\033[0m')
            return None
    except Exception as e:
        print(e)
        return None
#查询某个区块的状态信息
def get_block_status(hash):
    try:
        response = requests.get(f'https://btcscan.org/api/block/{hash}/status')
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            print('\033[31m' + response.text + '\033[0m')
            return None
    except Exception as e:
        print(e)
        return None
# 查询某个区块的交易信息最多返回25条，可以通过start_index参数指定起始位置
def get_block_transactions(hash, start_index=0):
    try:
        response = requests.get(f'https://btcscan.org/api/block/{hash}/txs/{start_index}')
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            print('\033[31m' + response.text + '\033[0m')
            return None
    except Exception as e:
        print(e)
        return None
# 查询某个区块的交易ID列表
def get_block_transaction_ids(hash):
    try:
        response = requests.get(f'https://btcscan.org/api/block/{hash}/txids')
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            print('\033[31m' + response.text + '\033[0m')
            return None
    except Exception as e:
        print(e)
        return None
# 查询指定区块内索引处的交易id
def get_block_transaction_id_by_index(hash, index):
    try:
        response = requests.get(f'https://btcscan.org/api/block/{hash}/txid/{index}')
        if response.status_code == 200:
            return response.text
        else:
            print('\033[31m' + response.text + '\033[0m')
            return None
    except Exception as e:
        print(e)
        return None
# 查询指定区块高度对应的区块哈希值
def get_block_hash_by_height(height):
    try:
        response = requests.get(f'https://btcscan.org/api/block-height/{height}')
        if response.status_code == 200:
            return response.text
        else:
            print('\033[31m' + response.text + '\033[0m')
            return None
    except Exception as e:
        print(e)
        return None
# GET /tx/:txid
# 查询指定交易ID的交易信息
def get_transaction_info_by_txid(txid):
    try:
        response = requests.get(f'https://btcscan.org/api/tx/{txid}')
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            print('\033[31m' + response.text + '\033[0m')
            return None
    except Exception as e:
        print(e)
        return None
# GET /tx/:txid/status
# 查询指定交易ID的交易状态信息
def get_transaction_status_by_txid(txid):
    try:
        response = requests.get(f'https://btcscan.org/api/tx/{txid}/status')
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            print('\033[31m' + response.text + '\033[0m')
            return None
    except Exception as e:
        print(e)
        return None
# GET /tx/:txid/merkle-proof
# 查询指定交易ID的默克尔证明
def get_transaction_merkleblock_proof_by_txid(txid):
    try:
        response = requests.get(f'https://btcscan.org/api/tx/{txid}/merkle-proof')
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            print('\033[31m' + response.text + '\033[0m')
            return None
    except Exception as e:
        print(e)
        return None
# GET /tx/:txid/outspend/:vout
# 查询指定交易ID的指定输出的支出信息
def get_transaction_outspend_by_txid_vout(txid, vout):
    try:
        response = requests.get(f'https://btcscan.org/api/tx/{txid}/outspend/{vout}')
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            print('\033[31m' + response.text + '\033[0m')
            return None
    except Exception as e:
        print(e)
        return None
# GET /tx/:txid/outspends
# 批量查询某交易所有输出的花费状态
def get_transaction_outspends_by_txid(txid):
    try:
        response = requests.get(f'https://btcscan.org/api/tx/{txid}/outspends')
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            print('\033[31m' + response.text + '\033[0m')
            return None
    except Exception as e:
        print(e)
        return None
# GET /address/:address
# 查询指定地址的余额信息
def get_address_balance_by_address(address):
    try:
        response = requests.get(f'https://btcscan.org/api/address/{address}')
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            print('\033[31m' + response.text + '\033[0m')
            return None
    except Exception as e:
        print(e)
        return None












if __name__ == '__main__':
    # print(get_latest_block_hash())
    # print(get_blocks_height())
    # print(get_single_block_info('00000000000000000000e48279196376ab69307801b9af0f53fe2443c133fbd9'))
    # print(get_block_status('00000000000000000000e48279196376ab69307801b9af0f53fe2443c133fbd9'))
    # print(get_block_transactions('00000000000000000000e48279196376ab69307801b9af0f53fe2443c133fbd9',25))
    # print(get_block_transaction_ids('00000000000000000000e48279196376ab69307801b9af0f53fe2443c133fbd9'))
    # print(get_block_transaction_id_by_index('00000000000000000000e48279196376ab69307801b9af0f53fe2443c133fbd9', 0))
    # print(get_block_hash_by_height(893219))
    # print(get_transaction_info_by_txid('389e8c4fdb680711586a4204596c515459c940f5bafb82354dff5bf780db5602'))
    # print(get_transaction_status_by_txid('389e8c4fdb680711586a4204596c515459c940f5bafb82354dff5bf780db5602'))
    # print(get_transaction_merkleblock_proof_by_txid('389e8c4fdb680711586a4204596c515459c940f5bafb82354dff5bf780db5602'))
    # print(get_transaction_outspend_by_txid_vout('0750dc1236838f167336630f62ef92c8848c09d8a175920772d9dfa773a3ef35', 0))
    # print(get_transaction_outspends_by_txid('0750dc1236838f167336630f62ef92c8848c09d8a175920772d9dfa773a3ef35'))
    print(get_address_balance_by_address('1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa'))

