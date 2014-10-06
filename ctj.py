#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
@file csv-to-json main
@module csv-to-json
@package csv-to-json
@subpackage main
@version 0.0.3
@author hex7c0 <hex7c0@gmail.com>
@copyright hex7c0 2014
@license GPLv3
'''

NAME = 'csv-to-json'
VERSION = '0.0.3'

try:
    # check version
    from sys import version_info
    if(version_info[0] < 3):
        print('must use Python 3 or greater')
        quit()
    del version_info
    # import
    from json import dump
    from csv import reader
    from time import time, gmtime, strftime
    from os.path import exists, isfile, isabs, abspath
    from argparse import ArgumentParser, ArgumentTypeError
except ImportError as error:
    print('in %s cannot load required libraries: %s!' \
        % (__name__, error))
    quit(1)

def ctj(args):
    '''
    build json file with selected args

    @param list args - parsed input
    @return: bool
    '''

    def populate(left, right, what=-1):
        '''
        popolate dictionary

        @param int left - first index
        @param int right - second index
        @param float what - element
        '''

        try:
            out[left][right] = what
        except KeyError:
            out[left] = {right: what}
        return

    body = False
    out = dict()
    if(args.w[0]):
        body = {args.w[0]: out}

    try:

        # read
        with open(args.csv[0]) as file:
            readed = reader(file, delimiter=args.d[0], quotechar=args.q[0])

        columns = next(readed)
        for row in readed:
            index = int(row[0])
            for element in range(1, len(row)):
                point = row[element]
                if(point == '0'):
                    populate(int(columns[element]), index)
                else:
                    try:
                        floated = float(point.replace(',', '.'))
                        populate(int(columns[element]), index, floated)
                    except ValueError:
                        pass

        # delimiter
        for height in out:
            point = out[height]
            clean = False
            for width in sorted(point):
                if(clean):  # remove next
                    del point[width]
                elif(point[width] == -1):
                    clean = True
            if(len(point) == 1):
                out[height] = -1

        # write
        with open(args.j[0], 'w') as file:
            dump(body or out, file, indent=args.i[0], sort_keys=args.s)
            file.write('\n')
        return True

    except KeyboardInterrupt:
        return False

if __name__ == '__main__':

    def check(root, out=True):
        '''
        type for argparse

        @param str root - path of file
        @return str|bool
        '''

        roo = root if isabs(root) else abspath(root)
        if(not exists(roo)):
            if(out):
                raise ArgumentTypeError('"%s" not found' % root)
            roo = False
        if(not isfile(roo)):
            if(out):
                raise ArgumentTypeError('"%s" not a file' % root)
            roo = False
        return roo

    def crono(start, pprint=True):
        '''
        given the initial unix time
        return time spent

        @param time start - stating time
        @param bool pprint - if print to output
        @return: str
        '''

        if(pprint):
            end = time() - start
            microsecond = int((end - int(end)) * 1000)
            if (end < 60):  # sec
                return '%s sec and %s ms' % (strftime('%S', \
                                                 gmtime(end)), microsecond)
            if (end < 3600):  # min
                return '%s min and %s ms' % (strftime('%M,%S', \
                                                 gmtime(end)), microsecond)
            # hr
            return '%s hr and %s ms' % (strftime('%H.%M,%S', \
                                                 gmtime(end)), microsecond)
        else:
            return int(strftime('%S', gmtime(start)))

    PARSER = ArgumentParser(description='Run %s' % NAME, prog=NAME)

    PARSER.add_argument('-v', '--version', action='version', \
                        version='%s version %s' % (NAME, VERSION))
    PARSER.add_argument('csv', type=check, nargs=1, help='path of csv file')

    GROUP_1 = PARSER.add_argument_group(title='csv parameters')
    GROUP_1.add_argument('-d', metavar='chars', nargs=1, type=str, \
                         help='delimiter for csv', default=[';'])
    GROUP_1.add_argument('-q', metavar='chars', nargs=1, type=str, \
                         help='quotechar for csv', default=['"'])

    GROUP_2 = PARSER.add_argument_group(title='json parameters')
    GROUP_2.add_argument('-j', metavar='path', nargs=1, type=str, \
                         help='path of json file', default=['ctj.json'])
    GROUP_2.add_argument('-w', metavar='object', nargs=1, type=str, \
                         help='wrapper for json', default=[False])
    GROUP_2.add_argument('-i', metavar='spaces', nargs=1, type=int, \
                         help='indent for json', default=[4])
    GROUP_2.add_argument('-s', action='store_false', \
                         help='sort keys for json')

    ARGV = PARSER.parse_args()

    START = time()
    if(ctj(ARGV)):
        if(not check(ARGV.j[0], False)):
            print('json not generated')
        else:
            print('json generated in %s' % crono(START))
    else:
        print('something wrong')
    quit(0)
