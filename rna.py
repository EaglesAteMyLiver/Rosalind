#!/usr/bin/env python3
# Rosalind RNA - eaml

def transcribe(string):
	return string.replace("T", "U")

if __name__ == "__main__":
	dataset = input("> ")
	print(transcribe(dataset))