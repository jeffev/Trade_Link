from entities.entidade_trade import Trade, SessionLocal

def criar_trade(data, duracao, ativo, tipo, qtde, direction, tendencia, sentimento, execucao, erro, timeframe, setup, pontos, valor, percentual, imagem, observacao):
    novo_trade = Trade(
        Data=data,
        Duracao=duracao,
        Ativo=ativo,
        Tipo=tipo,
        Qtde=qtde,
        Direction=direction,
        Tendencia=tendencia,
        Sentimento=sentimento,
        Execucao=execucao,
        Erro=erro,
        TimeFrame=timeframe,
        Setup=setup,
        Pontos=pontos,
        Valor=valor,
        Percentual=percentual,
        Imagem=imagem,
        Observacao=observacao
    )
    with SessionLocal() as session:
        session.add(novo_trade)
        session.commit()

def obter_trades():
    with SessionLocal() as session:
        return session.query(Trade).all()

def obter_trade_por_id(trade_id):
    with SessionLocal() as session:
        return session.query(Trade).filter(Trade.id == trade_id).first()

def atualizar_trade(trade_id, **kwargs):
    with SessionLocal() as session:
        trade = session.query(Trade).filter(Trade.id == trade_id).first()
        if trade:
            for key, value in kwargs.items():
                setattr(trade, key, value)
            session.commit()

def excluir_trade(trade_id):
    with SessionLocal() as session:
        trade = session.query(Trade).filter(Trade.id == trade_id).first()
        if trade:
            session.delete(trade)
            session.commit()
