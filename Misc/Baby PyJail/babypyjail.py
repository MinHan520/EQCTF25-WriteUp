# uncompyle6 version 3.9.2
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.11.8 (v3.11.8:db85d51d3e, Feb  6 2024, 18:02:37) [Clang 13.0.0 (clang-1300.0.29.30)]
# Embedded file name: pyjail.py
# Compiled at: 2024-07-09 14:51:51
# Size of source mod 2**32: 925 bytes
import sys as s, os as o

def m():
    f_l = ['flag', 'chr', '&', 'sh', 'system', 'bin', 'exec', 'import', 'stderr', 
     'stdout', 'sys', 'eval', 'read', 'os', '/', 'open', 'write', 'str']
    print("Enter your code (end with 'EOF') > ")
    d = ""
    while True:
        t = input()
        if t == "EOF":
            break
        else:
            d += t + "\n"

    print("Your code:\n", d)
    for i in f_l:
        if i in d:
            print("Wats mean u sorry2😔🤚🏻🤬Now u want to sorry me ⁉️😤😠NO🥵 why? Because this 🕰time banana 🍌already fruit 2 😱times 🤣👍🏻U think🤔 this heart 🤒is a plastic easily to recovery?😢Issa hurt mama 😞 heart is a hurt ☹️ heart a hurt 🤯😡 u a terrorist. Scram u smelly hacker ʕノ•ᴥ•ʔノ ︵ ┻━┻ 🩲")
            exit(0)

    c = compile(d, "<string>", "exec")
    o.close(0)
    o.close(1)
    exec(c)


if __name__ == "__main__":
    m()
