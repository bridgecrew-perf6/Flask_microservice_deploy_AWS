from main import translate, app

def test_translate():
    text = "一个人"
    assert (translate(text) == 'Alone.')

def test_translate():
    response = app.test_client().get("/")
    assert response.status_code == 200
