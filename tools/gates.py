"""Fails where a file under data/ holds a line FAIL; sleeps a little, like a real CI."""
import pathlib, sys, time
time.sleep(20)
bad = [str(p) for p in pathlib.Path("data").glob("*") if "FAIL" in p.read_text().split()]
print("bad:", bad or "none")
sys.exit(1 if bad else 0)
