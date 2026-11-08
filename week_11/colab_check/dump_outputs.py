"""Print every code cell's outputs from an executed notebook, one block per cell (for reading back a Colab run)."""
import json, sys
nb = json.load(open(sys.argv[1]))
for c in nb["cells"]:
    if c["cell_type"] != "code":
        continue
    print(f"##### {c['metadata'].get('id', '?')}")
    for o in c.get("outputs", []):
        if o["output_type"] == "stream":
            print("".join(o["text"]).rstrip())
        elif o["output_type"] in ("execute_result", "display_data"):
            print("".join(o["data"].get("text/plain", "")).rstrip())
        elif o["output_type"] == "error":
            print("ERROR", o["ename"], o["evalue"][:400])
print("##### END")
