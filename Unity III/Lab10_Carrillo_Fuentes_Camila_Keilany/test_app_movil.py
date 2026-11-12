import pytest
from app_movil import (
    PerfilMovil,
    PerfilPro,
    SuscripcionExpiradaError,
    PuntosInsuficientesError,
)

@pytest.fixture
def perfil_estandar():
    return PerfilMovil(username="KeyDev")


@pytest.fixture
def perfil_pro_valido():
    return PerfilPro(username="KeyPro", meses_suscripcion=3)


def test_inicializacion_perfil_movil(perfil_estandar):
    assert perfil_estandar.username == "KeyDev"
    assert perfil_estandar.gemas == 50
    assert perfil_estandar.racha_dias == 1
    assert perfil_estandar.notificaciones_activas is True


def test_gastar_gemas_exitoso(perfil_estandar):
    saldo_restante = perfil_estandar.gastar_gemas(20)
    assert saldo_restante == 30
    assert perfil_estandar.gemas == 30


def test_inicializacion_gemas_negativas():
    with pytest.raises(ValueError):
        PerfilMovil(username="TestUser", gemas=-10)


def test_gastar_gemas_insuficientes(perfil_estandar):
    with pytest.raises(PuntosInsuficientesError):
        perfil_estandar.gastar_gemas(100)


def test_descargar_contenido_suscripcion_expirada(perfil_pro_valido):
    perfil_pro_valido.meses_suscripcion = 0
    with pytest.raises(SuscripcionExpiradaError):
        perfil_pro_valido.descargar_contenido_offline()
    
    assert perfil_pro_valido.es_pro is False


@pytest.mark.parametrize("incremento,resultado_esperado", [
    (1, 51),
    (10, 60),
    (100, 150)
])
def test_ganar_gemas_parametrizado(perfil_estandar, incremento, resultado_esperado):
    assert perfil_estandar.ganar_gemas(incremento) == resultado_esperado


@pytest.mark.parametrize("invalid_increment", [0, -5, -100])
def test_ganar_gemas_invalidas_parametrizado(perfil_estandar, invalid_increment):
    with pytest.raises(ValueError):
        perfil_estandar.ganar_gemas(invalid_increment)


def test_jerarquia_y_herencia_perfil_pro(perfil_pro_valido):
    assert isinstance(perfil_pro_valido, PerfilPro)
    assert isinstance(perfil_pro_valido, PerfilMovil)


def test_inicializacion_perfil_pro_invalida():
    with pytest.raises(ValueError):
        PerfilPro(username="InvalidPro", meses_suscripcion=0)