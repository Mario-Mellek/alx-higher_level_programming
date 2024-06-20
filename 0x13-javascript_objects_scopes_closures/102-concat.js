#!/usr/bin/node
const fs = require('fs');
const args = process.argv;

const srcFile1 = args[2];
const srcFile2 = args[3];
const destFile = args[4];

const readFile1 = fs.readFileSync(srcFile1, 'utf8');
const readFile2 = fs.readFileSync(srcFile2, 'utf8');
const concatenatedData = readFile1 + readFile2;

fs.writeFileSync(destFile, concatenatedData, 'utf-8');
