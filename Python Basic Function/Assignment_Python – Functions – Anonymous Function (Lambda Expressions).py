def sum_10_values(*data):
    if len(data) != 10:
        return "Input harus terdiri dari 10 nilai"
    total = sum(data)

    return total

avg_10_value = lambda total : total / 10

value = [5,4,6,7,3,4,5,7,8,9]

total = sum_10_values(*value)

rata_rata = avg_10_value(total)

print(f'Total Nilai : {total}')
print(f'Rata-rata Nilai : {rata_rata}')