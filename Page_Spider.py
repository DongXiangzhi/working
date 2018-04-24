# import os
import argparse
from utilities import url_utilities


def main(database: str, url_list_file: str):
    big_word_list = []
    print('我们将使用数据库：' + database)
    print('我们将抓取以下页面：' + url_list_file)
    urls = url_utilities.load_urls_from_file(url_list_file)
    for url in urls:
        print('当前：' + url)
        page_content = url_utilities.load_page(url)
        words = url_utilities.scrape_page(page_content)
        big_word_list.extend(words)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-db", "--database", help="SQLite文件名称")
    parser.add_argument("-i", "--input", help="包含待抓取页面URL的文件")
    args = parser.parse_args()
    database_file = args.database
    input_file = args.input
    main(database=database_file, url_list_file=input_file)
