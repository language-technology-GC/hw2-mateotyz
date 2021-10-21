#!/usr/bin/env python
"""The program calcuates WER of the model."""

import csv


def main():
    with open('predictions.txt', "r") as source:
        reader=csv.reader(source, delimiter='\t')
        predictions = []

        #exclude irrelevant information
        for line in reader:
            if len(line) >1:
                predictions.append(line)

        count = 0 #initial count of incorrect predictions
        n = 0
        while n < len(predictions):
            target = predictions[n+1][1]
            hypothesis = predictions[n+2][2]
            if target != hypothesis:
                count += 1
            n += 5 #next word is 5 rows away
        
        # WER = count/100 * 100 = count
        print("WER:", count)


if __name__ == "__main__":
    main()
