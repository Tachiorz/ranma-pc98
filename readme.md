Default CS for ranma hdi image : 090f


Looking for print
-----------------

1000:3497 INT 18h AH 14h
INT 18h Function 14h: read font pattern 16 dot

       1000:3fd4 e8 66 f4        CALL       FUN_1000_343d                                    undefined FUN_1000_343d()
       1000:3f6d e8 04 00        CALL       FUN_1000_3f74                                    undefined FUN_1000_3f74()
       1000:37ea e8 78 07        CALL       FUN_1000_3f65                                    undefined FUN_1000_3f65(undefine
       1000:31b6 e8 28 06        CALL       FUN_1000_37e1                                    undefined FUN_1000_37e1(undefine

Print function FUN_1000_315f

       1000:2f1a e8 42 02        CALL       FUN_1000_315f                                    undefined FUN_1000_315f(undefine
       1000:2edf e8 30 00        CALL       FUN_1000_2f12                                    undefined FUN_1000_2f12()
       1000:2ea4 e8 1f 00        CALL       FUN_1000_2ec6                                    undefined FUN_1000_2ec6()

OP handler?

       1000:199b e8 fc 14        CALL       FUN_1000_2e9a                                    undefined FUN_1000_2e9a()

Opcode dispatch

       1000:04c3 e8 4c 00        CALL       FUN_1000_0512                                    undefined FUN_1000_0512()

Opcodes
-------
todo: untangle this clusterfuck

OP < 0x3f : FUN_1000_2499()
	while True:
		OP == 0x40 : break
		OP < 0x40 :
OP >= 0x3f and (OP < 0x60 or OP > 0xaf): \*(undefined2 \*)0x8726 = 1;
OP >= 0x60 and OP <= 0xaf : call [OP\*4 + 0x3c]


SCENE read
----------
$090f:9765 (12855): File A:SCENE_00.COM opened w/handle 0 (filename loc: 68fde)
$090f:9745 (12835): file 5: read 6000 bytes to $847b:0006 (847b6)


Tracking for start of SCENE interpretation
------------------------------------------
[0x8730] - instruction counter

initialised somwhere in  1000:026d CALL       FUN_1000_0407 from [0x8744]

