#!/usr/bin/env python
import sys
import time
import requests
import bs4

released_streams = {"ew", "radiative", "leptonic"}


def get_page(url: str) -> bs4.BeautifulSoup:
    for i in range(5):
        if (req := requests.get(url)).ok:
            break
        time.sleep(15 * i)
    else:
        req.raise_for_status()
    return bs4.BeautifulSoup(req.content, "html.parser")


def get_header_anchor_name(header: bs4.Tag) -> str:
    if (anchor := header.find("a")) is not None:
        return anchor["name"]
    return ""


def get_allowed_tables(url: str) -> list[bs4.Tag]:
    all_headings = get_page(url).find_all("h2")
    allowed_table_headings = filter(
        lambda h: get_header_anchor_name(h) in released_streams, all_headings
    )
    return [h.find_next_sibling("table") for h in allowed_table_headings]


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {__file__} <url>")
        exit()
    for table in get_allowed_tables(sys.argv[1]):
        print(table)