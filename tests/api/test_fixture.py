import pytest

@pytest.mark.check
def test_change_name(user):
    # user = User()
    # user.create()
    assert user.name == 'Serhii'
    # user.remove()

@pytest.mark.check
def test_change_second_name(user):
    # user = User()
    # user.create()
    assert user.second_name == 'Solomin'
    # user.remove()



