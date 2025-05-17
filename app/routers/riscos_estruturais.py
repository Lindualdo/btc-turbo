from fastapi import APIRouter

router = APIRouter()

# Mocked data for structural risks indicators
mock_data = {
    "model_variance": {
        "value": 0.15,
        "classification": "Baixo",
        "description": "Indica baixa volatilidade nos ativos."
    },
    "mvrv": {
        "value": 1.2,
        "classification": "Neutro",
        "description": "Atualmente, os ativos estão sobrevalorizados."
    },
    "vdd": {
        "value": 0.75,
        "classification": "Moderado",
        "description": "A média de preços indica uma tendência de baixa."
    },
    "fear_and_greed": {
        "value": 60,
        "classification": "Medo",
        "description": "Os investidores estão demonstrando sinais de medo."
    }
}

@router.get("/riscos-estruturais", summary="Análise de Riscos Estruturais", tags=["Riscos Estruturais"])
async def get_riscos_estruturais():
    """
    Retorna dados mockados sobre Riscos Estruturais do BTC.
    """
    return mock_data
