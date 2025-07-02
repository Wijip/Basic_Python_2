import re

def mask_phone(match):
    s = match.group()
    digits = re.findall(r'\d', s)
    n = len(digits)
    if n < 10 or n > 13:
        return s               # bukan nomor telepon target
    # hitung berapa digit yang harus di-mask
    to_mask = n - 4
    masked = []
    cnt = 0
    for ch in s:
        if ch.isdigit():
            if cnt < to_mask:
                masked.append('*')
            else:
                masked.append(ch)
            cnt += 1
        else:
            masked.append(ch)
    return ''.join(masked)

def main():
    inp = "contacts.txt"
    out = "contacts_masked.txt"
    text = open(inp, encoding='utf-8').read()
    # cari substring yang mengandung digit+separator panjang ≥10
    pattern = re.compile(r'[\d\-\+\s\(\)]{10,}')
    result = pattern.sub(mask_phone, text)
    open(out, 'w', encoding='utf-8').write(result)
    print(f"Masking selesai. Cek file {out}")

if __name__ == "__main__":
    main()
