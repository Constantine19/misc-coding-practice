# coding=utf-8
"""
Problem description: 
Given the api names and their respective start/end times, calculate
the average latency for each api.

┌─[~/Desktop/leetcode]
└──╼ cat test_file
get_foo start  2222222100
get_foo end    2222222150
get_foo start  2222222220
get_bar start  2222222200
get_bar end    2222222230
get_foo end    2222222250
┌─[~/Desktop/leetcode]
└──╼ cat test_file | python gg.py 
get_bar: average = 30
get_foo: average = 40

My Solution:

1.  Create a data structure like this:
{
"get_foo": {
    "start_times": [
        "2222222100",
        "2222222220"
        ], 
    "end_times": [
        "2222222150",
        "2222222250"
        ]
},
"get_bar" : {
    "start_times":[
        "2222222200"
    ],
    "end_times": [
        "2222222230"
    ]       
    }
}

2.  For each api, sum up all the start/end times, subtract end - start,
    and finally divide by the length of the list with times.

get_foo: average = 40
get_bar: average = 30

"""


def calculate_avg_latency(log):
    data = {}
    for i in range(len(log)):
        api, cmd, time = log[i].split()[0], log[i].split()[1], int(log[i].split()[2])

        if api not in data:
            data[api] = {'start': [time], 'end': []}
        else:
            if cmd == 'start':
                data[api]['start'].append(time)
            else:
                data[api]['end'].append(time)

    for key in data:
        avg = (sum(data[key]['end']) - sum(data[key]['start'])) / len(data[key]['start'])

        print "{}: average = {}".format(key, avg)


def main():
    with open('test_file') as f:
        log = f.readlines()

    calculate_avg_latency(log)


if __name__ == '__main__':
    main()
