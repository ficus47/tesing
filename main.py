import streamlit as st
import pathlib
import shutil
import logging
from bs4 import BeautifulSoup

adsense_url = "https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8075907034534804"
GA_AdSense = """
      <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8075907034534804"
     crossorigin="anonymous"></script>
    """

# Insert the script in the head tag of the static template inside your virtual
index_path = pathlib.Path(st.__file__).parent / "static" / "index.html"
st.write(f'editing {index_path}')
soup = BeautifulSoup(index_path.read_text(), features="html.parser")
if not soup.find("script", src=adsense_url): 
    bck_index = index_path.with_suffix('.bck')
    if bck_index.exists():
        shutil.copy(bck_index, index_path)  
    else:
        shutil.copy(index_path, bck_index)  
    html = str(soup)
    new_html = html.replace('<head>', '<head>\n' + GA_AdSense)
    index_path.write_text(new_html)