import re
from typing import List

import arxiv


def extract_arxiv_ids(text: str):
    pattern = re.compile(r"https://arxiv.org/pdf/(.*).pdf")
    all_matches = pattern.findall(text)

    ids = []
    for match in all_matches:
        ids.append(match)

    return ids


def download_arxiv_paper(arxiv_ids: List[str], local_folder: str):
    search = arxiv.Search(id_list=arxiv_ids)

    for paper in arxiv.Client().results(search):
        print(f"Downloading {paper}")
        paper.download_pdf(local_folder, f"{paper.title}.pdf")


text = open("./hallucination_reddit_post.txt", "r").readlines()
text = "\n".join(text)
ids = extract_arxiv_ids(text)

download_arxiv_paper(ids, local_folder="./hallucination_papers")
