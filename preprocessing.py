#!/usr/bin/env python
"""The program takes input data and outputs two files corresponding to each column."""


import argparse
import csv


def prepare_data(path_a, path_b, path_c):
    with open(path_a, "r") as source:
        with open(path_b, "w") as sink1, open(path_c, "w") as sink2:
            reader=csv.reader(source, delimiter='\t')
            for line in reader:
                grapheme = " ".join(line[0])
                phoneme = line[1]
                print(grapheme, file=sink1)
                print(phoneme, file=sink2)


def main(args: argparse.Namespace) -> None:
    prepare_data(args.input, args.output1, args.output2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Path of input data")
    parser.add_argument("output1", help="Path of output data for 1st column")
    parser.add_argument("output2", help="Path of output data for 2nd column")
    main(parser.parse_args())
