# CMU Binary Bomb

We get the following for phase_1 after disassembly.
```
phase_1:
  400ee0:	48 83 ec 08 	subq	$8, %rsp
  400ee4:	be 00 24 40 00 	movl	$4203520, %esi
  400ee9:	e8 4a 04 00 00 	callq	1098 <strings_not_equal>
  400eee:	85 c0 	testl	%eax, %eax
  400ef0:	74 05 	je	5 <phase_1+17>
  400ef2:	e8 43 05 00 00 	callq	1347 <explode_bomb>
  400ef7:	48 83 c4 08 	addq	$8, %rsp
  400efb:	c3 	retq
```

Looks like some simple string comparison. Let's fire up GDB and try to read the
string at that memory address.

```
$ gdb bomb
(gdb) layout asm # shows assembly line by line interactively
(gdb) start # start and break at main
(gdb) break phase_1 # breakpoint at phase_1 function
(gdb) continue # runs until breakpoints
random test string
(gdb) x/s 0x402400 # dereference string at memory location
0x402400: "Border relations with Canada have never been better."
```

You don't need the commands before `x/s 0x402400` technically, but they're
really nice to know.

![GDB Screenshot](https://github.com/UConnSec/Challenges/blob/master/2016-11-05 Week 2/BinaryBombPart1/Solution-GDB.png)
