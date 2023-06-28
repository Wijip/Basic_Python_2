import time

score = 0
def tambah_score():
    global score
    score += 1
    print("Score :",score)

# tambah_score()

for i in range(10):
    tambah_score()
    time.sleep(0.5)