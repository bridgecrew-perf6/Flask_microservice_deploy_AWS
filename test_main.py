from main import translate

def test_translate():
    text = "一个人"
    assert (translate(text) == 'Alone.')