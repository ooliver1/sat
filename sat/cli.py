# fmt: off
main = lambda: print("Usage: sat <filename>") if len(__import__("sys").argv) != 2 else (lambda data: print("\n".join(f"{'69'.zfill(len(str(len(data))))} | {line}" for line in data)))(open(__import__("sys").argv[1]).read().splitlines())
