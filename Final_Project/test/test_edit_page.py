import pytest
# pytest flask_sample -rA gives detailed output including print statements


@pytest.fixture()
def app():
    from ..main import create_app
    from ..sql.db import DB
    app = create_app()
    """app.config.update({
        "TESTING": True,
    })"""
    # insert dummy record to test at a negative index so it doesn't collide with valid values
    # note: this will likely still trigger auto_increment
    DB.insertOne("INSERT INTO IS601_Sample (id, name, val) VALUES (-1, 'tc','tcval')")
    # other setup can go here
    # update: id is not AUTO INCREMENTING

    yield app

    # clean up / reset resources here
    DB.delete("DELETE FROM IS601_Sample WHERE id = -1")


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

def test_edit_page(client):
    # https://www.scrapingbee.com/blog/python-web-scraping-beautiful-soup/
    response = client.get("/sample/edit?id=-1")
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(response.data, 'html.parser')
   
    form = soup.form
    ele = form.select("[name='value']")[0]
    print(ele)
    # for easier debugging run pytest with the -rP flags
    assert ele.get("value") == "tcval"