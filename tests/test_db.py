from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    new_user = User(
        username='caipora', password='caititu', email='caipora@folclore.br'
    )
    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.username == 'caipora'))

    assert user.username == 'caipora'
