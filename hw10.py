
import pickle
import os

def input_scores():
    scores = []
    i = 1
    while True:
        score = int(input(f"#{i}? "))
        if score < 0:
            break
        scores.append(score)
        i += 1
    return scores

def get_average(scores):
    return sum(scores) / len(scores)

def show_scores(scores):
    print("개인점수:", ' '.join(map(str, scores)))
    print(f"평균: {get_average(scores):.1f}")

def save_scores(scores, filename="score.bin"):
    with open(filename, "wb") as f:
        pickle.dump(scores, f)

def load_scores(filename="score.bin"):
    with open(filename, "rb") as f:
        return pickle.load(f)

def main():
    filename = "score.bin"

    if os.path.exists(filename):
        # 파일에서 읽기
        scores = load_scores(filename)
    else:
        # 사용자 입력
        scores = input_scores()
        save_scores(scores, filename)

    show_scores(scores)

main()