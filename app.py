from flask import Flask, jsonify, request, render_template
from api import *

app = Flask(__name__)

# HTML Routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/latest-block')
def latest_block():
    return render_template('latest_block.html')

@app.route('/block-height')
def block_height():
    return render_template('block_height.html')

@app.route('/block-info')
def block_info():
    return render_template('block_info.html')

@app.route('/block-status')
def block_status():
    return render_template('block_status.html')

@app.route('/block-transactions')
def block_transactions():
    return render_template('block_transactions.html')

@app.route('/block-transaction-ids')
def block_transaction_ids():
    return render_template('block_transaction_ids.html')

@app.route('/block-transaction-id-by-index')
def block_transaction_id_by_index():
    return render_template('block_transaction_id_by_index.html')

@app.route('/block-hash-by-height')
def block_hash_by_height():
    return render_template('block_hash_by_height.html')

@app.route('/transaction-info')
def transaction_info():
    return render_template('transaction_info.html')

@app.route('/transaction-status')
def transaction_status():
    return render_template('transaction_status.html')

@app.route('/transaction-merkle-proof')
def transaction_merkle_proof():
    return render_template('transaction_merkle_proof.html')

@app.route('/transaction-outspend')
def transaction_outspend():
    return render_template('transaction_outspend.html')

@app.route('/transaction-outspends')
def transaction_outspends():
    return render_template('transaction_outspends.html')

@app.route('/address-balance')
def address_balance():
    return render_template('address_balance.html')

# API Routes
@app.route('/api/blocks/tip/hash', methods=['GET'])
def latest_block_hash():
    result = get_latest_block_hash()
    return jsonify({'hash': result} if result else {'error': '无法获取最新区块哈希'})

@app.route('/api/blocks/tip/height', methods=['GET'])
def blocks_height():
    result = get_blocks_height()
    return jsonify({'height': result} if result else {'error': '无法获取区块高度'})

@app.route('/api/block/<hash>', methods=['GET'])
def single_block_info(hash):
    result = get_single_block_info(hash)
    return jsonify(result if result else {'error': '无法获取区块信息'})

@app.route('/api/block/<hash>/status', methods=['GET'])
def block_status_api(hash):
    result = get_block_status(hash)
    return jsonify(result if result else {'error': '无法获取区块状态'})

@app.route('/api/block/<hash>/txs', methods=['GET'])
def block_transactions_api(hash):
    start_index = request.args.get('start_index', default=0, type=int)
    result = get_block_transactions(hash, start_index)
    if start_index %25 != 0:
        return jsonify({'error': 'start_index 必须为 25 的倍数'})
    return jsonify(result if result else {'error': '无法获取区块交易列表'})

@app.route('/api/block/<hash>/txids', methods=['GET'])
def block_transaction_ids_api(hash):
    result = get_block_transaction_ids(hash)
    return jsonify(result if result else {'error': '无法获取区块交易 ID 列表'})

@app.route('/api/block/<hash>/txid/<int:index>', methods=['GET'])
def block_transaction_id_by_index_api(hash, index):
    result = get_block_transaction_id_by_index(hash, index)
    return jsonify({'txid': result} if result else {'error': '无法获取指定索引的交易 ID'})

@app.route('/api/block-height/<int:height>', methods=['GET'])
def block_hash_by_height_api(height):
    result = get_block_hash_by_height(height)
    return jsonify({'hash': result} if result else {'error': '无法获取指定高度的区块哈希'})

@app.route('/api/tx/<txid>', methods=['GET'])
def transaction_info_by_txid_api(txid):
    result = get_transaction_info_by_txid(txid)
    return jsonify(result if result else {'error': '无法获取交易信息'})

@app.route('/api/tx/<txid>/status', methods=['GET'])
def transaction_status_by_txid_api(txid):
    result = get_transaction_status_by_txid(txid)
    return jsonify(result if result else {'error': '无法获取交易状态'})

@app.route('/api/tx/<txid>/merkle-proof', methods=['GET'])
def transaction_merkleblock_proof_by_txid_api(txid):
    result = get_transaction_merkleblock_proof_by_txid(txid)
    return jsonify(result if result else {'error': '无法获取默克尔证明'})

@app.route('/api/tx/<txid>/outspend/<int:vout>', methods=['GET'])
def transaction_outspend_by_txid_vout_api(txid, vout):
    result = get_transaction_outspend_by_txid_vout(txid, vout)
    return jsonify(result if result else {'error': '无法获取输出支出信息'})

@app.route('/api/tx/<txid>/outspends', methods=['GET'])
def transaction_outspends_by_txid_api(txid):
    result = get_transaction_outspends_by_txid(txid)
    return jsonify(result if result else {'error': '无法获取所有输出支出状态'})

@app.route('/api/address/<address>', methods=['GET'])
def address_balance_by_address_api(address):
    result = get_address_balance_by_address(address)
    return jsonify(result if result else {'error': '无法获取地址余额'})

if __name__ == '__main__':
    app.run(debug=True)