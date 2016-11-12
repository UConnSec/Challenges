# Broken ICO Solution

Let's start with a hex dump of the file we're given. We were told that only
the beginning of the file was broken.

```sh
$ cat mysteriousfile | xxd
00000000: be00 0100 0100 0000 1000 0100 0400 e007  ................
00000010: 0000 1600 0000 0d0a 1a0a 0000 000d 4948  ..............IH
00000020: 4452 0000 0280 0000 0190 0806 0000 003e  DR.............>
00000030: f3d1 2500 0007 a749 4441 5478 9ced d641  ..%....IDATx...A
00000040: 4e03 3110 0041 9b4f ee3e d179 a539 0591  N.1..A.O.>.y.9..
00000050: e490 2010 4874 d571 34b2 463e f55c 6bed  .. .Ht.q4.F>.\k.
00000060: 71e7 388e 31e7 bc1f 8fbd f7b8 5c2e 37b3  q.8.1.......\.7.
00000070: f33c 6fe6 e779 8eb5 d638 8ee3 61f7 bb6f  .<o..y...8..a..o
00000080: 5f67 3f79 cbe7 dd57 6f79 f5bd affe c3ab  _g?y...Woy......
00000090: b73e 9b5f 6f9d 738e b5d6 c71e 00c0 1863  .>._o.s........c
```

The ico file format says that the first byte should be `00`. This is not the
case. Let's correct it.

```sh
$ cat mysteriousfilefix1 | xxd
00000000: 0000 0100 0100 0000 1000 0100 0400 e007  ................
00000010: 0000 1600 0000 0d0a 1a0a 0000 000d 4948  ..............IH
00000020: 4452 0000 0280 0000 0190 0806 0000 003e  DR.............>
00000030: f3d1 2500 0007 a749 4441 5478 9ced d641  ..%....IDATx...A
```

We see part of the PNG file header in here as well `0d0a1a0a`. Let's correct
that.

```sh
$ cat mysteriousfilefix2.ico | xxd
00000000: 0000 0100 0100 0000 1000 0100 0400 e007  ................
00000010: 0000 1600 0000 8950 4e47 0d0a 1a0a 0000  .......PNG......
00000020: 000d 4948 4452 0000 0280 0000 0190 0806  ..IHDR..........
00000030: 0000 003e f3d1 2500 0007 a749 4441 5478  ...>..%....IDATx
00000040: 9ced d641 4e03 3110 0041 9b4f ee3e d179  ...AN.1..A.O.>.y
00000050: a539 0591 e490 2010 4874 d571 34b2 463e  .9.... .Ht.q4.F>
```

Now we get a large file with some weird encoding at the top. Well, CTF problems
for some reason love morse code, so let's try that.

```
..... ----- ....- ..-. ..... ----- ....- ...-- ....- ..-. ..... ..--- ....- . ..... ----. ..... ..... ....- -..
```

Converted to letters and numbers:

```
504f50434f524e59554d
```

Ok, one more layer here. Looks like the range of this string is 0-9A-F.
Possibly hexadecimal?

```
POPCORNYUM
```
