actor_name = input()
academy_points = float(input())
num_evaluators = int(input())
total_points = academy_points

for _ in range(num_evaluators):
    evaluator_name = input()
    evaluator_points = float(input())
    points_from_evaluator = len(evaluator_name) * evaluator_points / 2
    total_points += points_from_evaluator
    if total_points > 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
        break
else:
    needed_points = 1250.5 - total_points
    print(f"Sorry, {actor_name} you need {needed_points:.1f} more!")