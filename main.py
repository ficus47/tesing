import streamlit as st
import pathlib
from streamlit_javascript import st_javascript

GA_AdSense = """
      <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8075907034534804"
     crossorigin="anonymous"></script>
    """

# Insert the script in the head tag of the static template inside your virtual
index_path = pathlib.Path(st.__file__).parent / "static" / "index.html"
st.write(index_path)
st_javascript(f"""
    const head = document.getElementsByTagName('head')[0];
    const script = document.createElement('script');
    script.async = true;
    script.src = 'https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8075907034534804';
    head.appendChild(script);

    const ins = document.createElement('ins');
    ins.className = 'adsbygoogle';
    ins.style = 'display:block';
    ins.setAttribute('data-ad-client', 'ca-pub-8075907034534804');
    ins.setAttribute('data-ad-slot', 'f08c47fec0942fa0');
    ins.setAttribute('data-ad-format', 'auto');
    ins.setAttribute('data-full-width-responsive', 'true');
    document.body.appendChild(ins);

    (adsbygoogle = window.adsbygoogle || []).push({{}});
""")

open("/home/adminuser/venv/lib/python3.11/site-packages/streamlit/static/sw.js", "r").write(open("sw.js", "r").read())