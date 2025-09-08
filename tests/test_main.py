def test_code_smell():
    response = client.get("/code_smell")
    assert response.status_code == 200
    # ตรวจแค่ substring → test ผ่าน
    assert "FastAPI" in response.json()["message"]
