import math
import os
import struct
import zlib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, "docs", "icons")

BG = (20, 17, 12)
GOLD = (245, 166, 35)

SEGMENTS = [
    ((0.34, 0.30), (0.20, 0.50)),
    ((0.20, 0.50), (0.34, 0.70)),
    ((0.455, 0.74), (0.545, 0.26)),
    ((0.66, 0.30), (0.80, 0.50)),
    ((0.80, 0.50), (0.66, 0.70)),
]
STROKE = 0.10
FEATHER = 0.015


def seg_dist2(px, py, a, b):
    ax, ay = a
    bx, by = b
    dx, dy = bx - ax, by - ay
    length_sq = dx * dx + dy * dy
    if length_sq == 0:
        return (px - ax) ** 2 + (py - ay) ** 2
    t = max(0.0, min(1.0, ((px - ax) * dx + (py - ay) * dy) / length_sq))
    cx, cy = ax + t * dx, ay + t * dy
    return (px - cx) ** 2 + (py - cy) ** 2


def render(size):
    half_w = STROKE * size / 2
    feather = FEATHER * size
    rows = []
    for y in range(size):
        ny = (y + 0.5) / size
        row = bytearray()
        for x in range(size):
            nx = (x + 0.5) / size
            d = math.sqrt(min(seg_dist2(nx, ny, a, b) for a, b in SEGMENTS)) * size
            cov = max(0.0, min(1.0, (half_w + feather - d) / (2 * feather)))
            row += bytes((
                int(GOLD[0] * cov + BG[0] * (1 - cov)),
                int(GOLD[1] * cov + BG[1] * (1 - cov)),
                int(GOLD[2] * cov + BG[2] * (1 - cov)),
                255,
            ))
        rows.append(bytes(row))
    return rows


def chunk(tag, data):
    return struct.pack(">I", len(data)) + tag + data + struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF)


def write_png(path, size):
    rows = render(size)
    raw = b"".join(b"\x00" + row for row in rows)
    ihdr = struct.pack(">IIBBBBB", size, size, 8, 6, 0, 0, 0)
    png = (b"\x89PNG\r\n\x1a\n"
           + chunk(b"IHDR", ihdr)
           + chunk(b"IDAT", zlib.compress(raw, 9))
           + chunk(b"IEND", b""))
    with open(path, "wb") as f:
        f.write(png)
    print(f"wrote {path} ({size}x{size}, {len(png)} bytes)")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    for size in (180, 192, 512):
        write_png(os.path.join(OUT_DIR, f"icon-{size}.png"), size)


if __name__ == "__main__":
    main()
