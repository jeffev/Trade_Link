from flask import jsonify, request
from server import app
from entities.entidade_trade import Trade, SessionLocal, criar_trade, obter_trades, obter_trade_por_id, atualizar_trade, excluir_trade

@app.route('/api/trades', methods=['POST'])
def criar_trade_endpoint():
    data = request.json.get('data')
    duracao = request.json.get('duracao')
    # Continue pegando os outros parâmetros do trade

    criar_trade(data, duracao, ativo, tipo, qtde, direction, tendencia, sentimento, execucao, erro, timeframe, setup, pontos, valor, percentual, imagem, observacao)
    
    return jsonify({'message': 'Trade criado com sucesso!'})

@app.route('/api/trades', methods=['GET'])
def obter_trades_endpoint():
    trades = obter_trades()
    trades_json = [{'id': trade.id, 'data': str(trade.Data), 'ativo': trade.Ativo, 'observacao': trade.Observacao} for trade in trades]
    return jsonify({'trades': trades_json})

@app.route('/api/trades/<int:trade_id>', methods=['GET'])
def obter_trade_por_id_endpoint(trade_id):
    trade = obter_trade_por_id(trade_id)
    if trade:
        trade_json = {'id': trade.id, 'data': str(trade.Data), 'ativo': trade.Ativo, 'observacao': trade.Observacao}
        return jsonify({'trade': trade_json})
    else:
        return jsonify({'message': 'Trade não encontrado'}), 404

@app.route('/api/trades/<int:trade_id>', methods=['PUT'])
def atualizar_trade_endpoint(trade_id):
    # Pegar os parâmetros da requisição e passar para a função atualizar_trade
    atualizar_trade(trade_id, **request.json)
    return jsonify({'message': 'Trade atualizado com sucesso!'})

@app.route('/api/trades/<int:trade_id>', methods=['DELETE'])
def excluir_trade_endpoint(trade_id):
    excluir_trade(trade_id)
    return jsonify({'message': 'Trade excluído com sucesso!'})
