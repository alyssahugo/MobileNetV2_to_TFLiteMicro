# convert_mem.py
input_file = "instmem.mem"
output_file = "instmem_bytes.mem"

with open(input_file) as f_in, open(output_file, "w") as f_out:
    for line in f_in:
        line = line.strip()
        if not line or line.startswith("@"):
            continue
        bytes_list = line.split()
        # process 4 bytes at a time
        for i in range(0, len(bytes_list), 4):
            b0, b1, b2, b3 = bytes_list[i:i+4]
            # reverse each 16-bit half
            half1 = b1 + b0
            half2 = b3 + b2
            f_out.write(half1.lower() + "\n")
            f_out.write(half2.lower() + "\n")
