from flask import Flask, jsonify, request
from backend.operations.operations_trades import criar_trade, obter_trades, obter_trade_por_id, atualizar_trade, excluir_trade

endpoint_app = Flask(__name__)

from flask import jsonify, request

@endpoint_app.route('/api/trades', methods=['POST'])
def criar_trade_endpoint():
    try:
        if request.is_json:
            data = request.json.get('data')
            duracao = request.json.get('duracao')
            ativo = request.json.get('ativo')
            tipo = request.json.get('tipo')
            qtde = request.json.get('qtde')
            direction = request.json.get('direction')
            tendencia = request.json.get('tendencia')
            sentimento = request.json.get('sentimento')
            execucao = request.json.get('execucao')
            erro = request.json.get('erro')
            timeframe = request.json.get('timeframe')
            setup = request.json.get('setup')
            pontos = request.json.get('pontos')
            valor = request.json.get('valor')
            percentual = request.json.get('percentual')
            imagem = request.json.get('imagem')
            observacao = request.json.get('observacao')

            criar_trade(data, duracao, ativo, tipo, qtde, direction, tendencia, sentimento, execucao, erro, timeframe, setup, pontos, valor, percentual, imagem, observacao)

            return jsonify({'message': 'Trade criado com sucesso!'})
        else:
            return jsonify({'error': 'A requisição não contém dados JSON'}), 400
    except Exception as e:
        return jsonify({'error': f'Erro ao processar a requisição: {str(e)}'}), 500


@endpoint_app.route('/api/trades', methods=['GET'])
def obter_trades_endpoint():
    try:
        trades = obter_trades()

        if trades is not None:
            trades_json = [{'id': trade.id, 'data': str(trade.Data), 'ativo': trade.Ativo, 'observacao': trade.Observacao} for trade in trades]
            return jsonify({'trades': trades_json})
        else:
            return jsonify({'error': 'Nenhum trade encontrado'}), 404
    except Exception as e:
        return jsonify({'error': f'Erro ao processar a requisição: {str(e)}'}), 500

@endpoint_app.route('/api/trades/<int:trade_id>', methods=['GET'])
def obter_trade_por_id_endpoint(trade_id):
    trade = obter_trade_por_id(trade_id)
    if trade:
        trade_json = {'id': trade.id, 'data': str(trade.Data), 'ativo': trade.Ativo, 'observacao': trade.Observacao}
        return jsonify({'trade': trade_json})
    else:
        return jsonify({'message': 'Trade não encontrado'}), 404

@endpoint_app.route('/api/trades/<int:trade_id>', methods=['PUT'])
def atualizar_trade_endpoint(trade_id):
    try:
        data = request.json.get('data')
        duracao = request.json.get('duracao')
        ativo = request.json.get('ativo')
        tipo = request.json.get('tipo')
        qtde = request.json.get('qtde')
        direction = request.json.get('direction')
        tendencia = request.json.get('tendencia')
        sentimento = request.json.get('sentimento')
        execucao = request.json.get('execucao')
        erro = request.json.get('erro')
        timeframe = request.json.get('timeframe')
        setup = request.json.get('setup')
        pontos = request.json.get('pontos')
        valor = request.json.get('valor')
        percentual = request.json.get('percentual')
        imagem = request.json.get('imagem')
        observacao = request.json.get('observacao')

        atualizar_trade(
            trade_id,
            data=data,
            duracao=duracao,
            ativo=ativo,
            tipo=tipo,
            qtde=qtde,
            direction=direction,
            tendencia=tendencia,
            sentimento=sentimento,
            execucao=execucao,
            erro=erro,
            timeframe=timeframe,
            setup=setup,
            pontos=pontos,
            valor=valor,
            percentual=percentual,
            imagem=imagem,
            observacao=observacao
        )

        return jsonify({'message': 'Trade atualizado com sucesso!'})
    except Exception as e:
        return jsonify({'error': f'Erro ao processar a requisição: {str(e)}'}), 500

@endpoint_app.route('/api/trades/<int:trade_id>', methods=['DELETE'])
def excluir_trade_endpoint(trade_id):
    try:
        excluir_trade(trade_id)
        return jsonify({'message': 'Trade excluído com sucesso!'})
    except Exception as e:
        return jsonify({'error': f'Erro ao excluir o trade: {str(e)}'}), 500
