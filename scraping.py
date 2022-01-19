def extract_title(soup: BeautifulSoup) -> str:
    return soup.title.get_text()
  
  
def extract_all_tags(html_content: list[Tag]) -> list[str]:
    return [tag.name for tag in html_content]
  

def extract_html_content(soup: BeautifulSoup) -> list[Tag]:
    return soup.find("div", attrs={"class": "td-post-content"}).find_all()
  

def extract_content(soup: BeautifulSoup) -> str:
    
    def remove_double_newlines(strings: list[str]) -> list[str]:
        return [string for string in strings if string]
    
    def extract_html_content(soup: BeautifulSoup) -> list[Tag]:
        return soup.find("div", attrs={"class": "td-post-content"}).find_all()
    
    article_text = []
    
    for content in extract_html_content(soup):
        if (content.name == "strong") or (content.name == "pre"):
            continue
    
        article_text.append(content.get_text())
    
    return "\n\n".join(remove_double_newlines(article_text))
  

def write_article(filename: str, soup: BeautifulSoup) -> None:
    with open(filename, "w") as f:
        f.write(extract_title(soup))
        f.write("\n\n")
        f.write(extract_content(soup))
