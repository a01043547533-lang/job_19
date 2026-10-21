from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup


def search_incruit(keyword, pages=1):
    jobs = []
    for i in range(pages):
        response = requests.get(
            "https://search.incruit.com/list/search.asp",
            params={"col": "job", "kw": keyword, "startno": i * 30},
            timeout=(5, 15),
        )
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        for li in soup.select("li.c_col"):
            company = li.select_one("a.cpname")
            title = li.select_one("div.cell_mid a")
            location = li.select_one("div.cl_md span")
            if company is None or title is None or not title.get("href"):
                continue
            jobs.append({
                "company": company.get_text(strip=True),
                "title": title.get_text(strip=True),
                "location": location.get_text(strip=True) if location else "",
                "link": urljoin(response.url, title["href"]),
            })
    return jobs
