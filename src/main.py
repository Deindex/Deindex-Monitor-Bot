from monitor.index_checker import check_url


def main():

    url = "https://deindex.fyi"

    result = check_url(url)

    print(result)


if __name__ == "__main__":
    main()
