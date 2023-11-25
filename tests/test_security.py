from jose import jwt

from fast_zero.security import SECRET_KEY, create_access_token


def test_jwt():
    data = {'teste': 'teste'}
    token = create_access_token(data)

    decoded = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])

    assert decoded['teste'] == data['teste']
    assert decoded['exp']  # Testa se o valor de exp foi adicionado ao token
