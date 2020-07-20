from tabulate import tabulate

ip_frequency = {}
url_frequency = {}


def process_line(line):
    global ip_frequency
    global url_frequency
    words = line.split()
    if words[0] in ip_frequency:
        ip_frequency[words[0]] += 1
    else:
        ip_frequency[words[0]] = 1

    for i in range(len(words)):
        word = words[i].strip('"')
        if word in ['GET', 'OPTIONS']:
            url = words[i + 1]
            if url in url_frequency:
                url_frequency[url] += 1
            else:
                url_frequency[url] = 1


def display_results():
    ip_table = sorted(ip_frequency.items(), key=lambda x: x[1], reverse=True)
    url_table = sorted(url_frequency.items(), key=lambda x: x[1], reverse=True)
    print(tabulate(ip_table, headers=('IP', 'FREQUENCY'), tablefmt='pretty'))
    print(tabulate(url_table, headers=('URL', 'FREQUENCY'), tablefmt='pretty'))


def main():
    filename = 'log.txt'
    try:
        for line in open(filename):
            if line == '\n':
                continue
            process_line(line)

    except FileNotFoundError:
        print("Sorry, couldn't find", filename + '.')
    except:
        print("Sorry, could not read", filename)

    display_results()


if __name__ == '__main__':
    main()
