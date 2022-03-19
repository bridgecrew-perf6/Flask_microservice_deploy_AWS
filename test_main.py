from main import translate

def test_translate():
    text = "一个人"
    assert (translate(text) == 'Alone.')
    
def test_home():
    response = app.test_client().get("/")
    assert response.status_code == 200

def test_translate():
    response = app.test_client().get("/translate")
    assert response.status_code == 200
