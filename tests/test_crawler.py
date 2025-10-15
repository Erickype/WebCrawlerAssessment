import requests_mock
from crawler import fetch_entries

HTML = """
<html>
<body>
  <tr class='athing' id='1'>
    <td class='title'>
      <span class='rank'>1.</span>
      <span class='titleline'><a href='url'>Example Title</a></span>
    </td>
  </tr>
  <tr><td class='subtext'>
    <span class='score'>42 points</span>
    <a href='item?id=1'>10 comments</a>
  </td></tr>
</body>
</html>
"""

def test_fetch_entries():
    with requests_mock.Mocker() as m:
        m.get("https://news.ycombinator.com/", text=HTML)
        entries = fetch_entries()
        assert len(entries) == 1
        assert entries[0].title == "Example Title"
        assert entries[0].points == 42
        assert entries[0].comments == 10
