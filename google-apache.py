"""
Question:
    Find the top ten most frequent IP addresses from a web server log file.

Example:
    14716104719,GET,/index.html,10.10.10.1
    14716104719,GET,/index.html,10.10.10.22
    14716104719,GET,/index.html,10.10.10.2
    14716104719,GET,/index.html,10.10.10.22
"""


def find_top_ten_most_frequent_ips(log):
    count = {}
    values = []
    for i in log:
        ip = i.split(',')[3].replace('\n', '')
        if ip not in count:
            count[ip] = 1
        else:
            count[ip] += 1

    for value in count.values():
        values.append(value)
    sorted_values = sorted(values, reverse=True)

    print "Most Frequent IPs"
    for i in sorted_values[:10]:
        for key, value in count.items():
            print "Rank# {} --> IP {}".format(sorted_values[i], key)

        # print "Rank# {} --> IP {}".format(sorted_values[i], count.keys())



def main():
    with open('google-apache-test-file') as f:
        log = f.readlines()

    find_top_ten_most_frequent_ips(log)


if __name__ == '__main__':
    main()
