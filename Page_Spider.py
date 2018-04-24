import os
import argparse


def main(database: str, url_list_file: str):
    print('我们将使用数据库：' + database);
    print('我们将抓取以下页面：' + url_list_file);


if __name__ == "__main__":
    parser = argparse.ArgumentParser();
    parser.add_argument("-db", "--database", help="SQLite文件名称")
    parser.add_argument("-i", "--input", help="包含待抓取页面URL的文件")
    args = parser.parse_args()
    database_file = args.database
    input_file = args.input
    main(database=database_file, url_list_file=input_file)
