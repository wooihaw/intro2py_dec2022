import sys
print(f"{sys.argv=}")

if len(sys.argv) < 2:
    print("You need to provide an integer after the script name.")
    print("E.g.: python sys_argv.py 12")
    sys.exit()

num = int(sys.argv[1])
print(num * "Hello ")
