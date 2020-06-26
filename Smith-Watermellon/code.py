
import sys
from sys import argv

seq1 = "ACATGCTACACGTATCCGATACCCCGTAACCGATAACGATACACAGACCTCGTACGCTTGCTACAACGTACTCTATAACCGAGAACGATTGACATGCCTCGTACACATGCTACACGTACTCCGAT"
seq2 = "ACATGCGACACTACTCCGATACCCCGTAACCGATAACGATACAGAGACCTCGTACGCTTGCTAATAACCGAGAACGATTGACATTCCTCGTACAGCTACACGTACTCCGATGATCGATAAGTCAT"

s1 = seq1[:60]
s2 = seq1[61:120]
s3 = seq1[121:125]

ss1 = seq2[:60]
ss2 = seq2[61:106]
ss3 = seq2[107:111]

match = +2
mismatch = -2
gap = -2

row = len(seq1)
col = len(seq2)


def gen_value(I, J):
    if I == row-1 or J == col-1:
        return Arr[I][J]
    else:
        highCel = Arr[I+1][J+1]

        for i in range(I+1, row):
            highCel = max(highCel, Arr[i][J]+gap)
        for j in range(J+1, col):
            highCel = max(highCel, Arr[I][j]+gap)
        return Arr[I][J] + highCel


def make_matrix(row, col, mismatch):
    A1 = [mismatch] * row
    for i in range(row):
        A1[i] = [mismatch] * col
    return A1


def process_matrix(row, col, seqA, seqB, match):
    for i in range(row):
        for j in range(col):
            if seqA[i] == seqB[j]:
                Arr[i][j] = match
    return Arr


def final_matrix(row, col, gap):
    for i in range(row-1, -1, -1):
        for j in range(col-1, -1, -1):
            Arr[i][j] = gen_value(i, j)
    return Arr


def print_matrix():
    for i in range(row):
        print("{}".format(Arr[i]))


def trace_back(i, j, target):
    if i == row-1 or j == col-1:
        return [seq1[i], seq2[i]]
    else:
        max_trace = max(Arr[i+1][j+1], Arr[i][j+1], Arr[i+1][j])
        if Arr[i+1][j+1] == max_trace:
            list = trace_back(i+1, j+1, "Good Flow")
        elif Arr[i][j+1] == max_trace:
            list = trace_back(i, j+1, "Jump row")
        else:
            list = trace_back(i+1, j, "jump col")

        partA = seq1[i]
        partB = seq2[j]
        if target == "jump row":
            partA = "-"
        elif target == "jump col":
            partB = "-"
        return [partA+list[0], partB+list[1]]


def mid_val(traced):
    mide = ""
    for k in range(0, len(traced[0])):
        mid = "."
        if traced[0][k] == traced[1][k]:
            mid = "|"
        mide = mide + mid
    return mide



Arr = make_matrix(row, col, mismatch)

Arr = process_matrix(row, col, seq1, seq2, match)

Arr = final_matrix(row, col, gap)


traced = trace_back(0, 0, "normal")
mid = mid_val(traced)

print("{}\n{}\n{}".format(traced[0], mid, traced[1]))

